import re
import shutil
from pathlib import Path
from typing import NewType

import yaml

# Configuration
OBSIDIAN_VAULT_PATH = Path("/Users/fabio/Google Drive/My Drive/obsiabio")
OBSIDIAN_TRASH_FOLDER_NAME = ".trash"
TARGET_YAML_KEY = "tags"
TARGET_TAG_VALUE = "tech/website/hosted"
TEMP_FOLDER_PATH = Path("_tmp/obsidian_publish")
WEBSITE_NOTES_PATH = Path("../notes")
WEBSITE_ASSETS_PATH = Path("../assets/images")

Frontmatter = NewType("Frontmatter", dict)
MdContent = NewType("MdContent", str)


def mirror_obsidian_notes() -> None:
    """
    Finds notes with the publish tag in Obsidian vault,
    cleans their filenames, and copies them to the temp folder.
    """
    print(f"Starting mirror process...")
    print(f"Source Vault: {OBSIDIAN_VAULT_PATH}")
    print(f"Target Tag: '{TARGET_TAG_VALUE}'")
    print(f"Temp Folder: {TEMP_FOLDER_PATH}")
    print(f"Website Assets Folder: {WEBSITE_ASSETS_PATH}")

    if TEMP_FOLDER_PATH.exists():
        print(f"Clearing existing temp folder: {TEMP_FOLDER_PATH}")
        shutil.rmtree(TEMP_FOLDER_PATH)
    TEMP_FOLDER_PATH.mkdir(parents=True, exist_ok=True)
    WEBSITE_ASSETS_PATH.mkdir(parents=True, exist_ok=True)

    copied_count = 0
    for item in OBSIDIAN_VAULT_PATH.rglob('*.md'):
        if OBSIDIAN_TRASH_FOLDER_NAME in item.parts:
            continue
        if item.is_file():
            obsidian_frontmatter, content = _parse_markdown_file(item)
            if _has_publish_tag(obsidian_frontmatter):
                # Process images
                new_content = content
                image_links = _extract_image_links(content)
                for link in image_links:
                    image_path = _resolve_image_path(link, item.parent)
                    if image_path:
                        cleaned_image_name = _clean_filename(image_path.name)
                        target_image_path = WEBSITE_ASSETS_PATH / cleaned_image_name
                        shutil.copy2(image_path, target_image_path)
                        new_link_path = f"/assets/images/{cleaned_image_name}"
                        new_content = _update_image_link_in_content(new_content, link, new_link_path)

                web_name = _clean_filename(item.name)
                target_path = TEMP_FOLDER_PATH / web_name
                try:
                    # Save the modified content and original frontmatter
                    _save_markdown_file(target_path, obsidian_frontmatter, new_content)
                    copied_count += 1
                except Exception as e:
                    print(f"Error saving {item} to {target_path}: {e}")
    print(f"Mirroring complete. Copied {copied_count} notes to {TEMP_FOLDER_PATH}")


def sync_notes() -> None:
    """
    Compares the temp folder with the website notes folder and updates the website notes in the working directory.
    """
    print("\nStarting sync process...")
    print(f"Comparing '{TEMP_FOLDER_PATH}' with '{WEBSITE_NOTES_PATH}'")

    assert TEMP_FOLDER_PATH.exists(), f"{TEMP_FOLDER_PATH=} does not exist. Run mirroring first."
    assert WEBSITE_NOTES_PATH.exists(), f"{WEBSITE_NOTES_PATH=} not found."

    temp_obsidian_notes = {f.name: f for f in TEMP_FOLDER_PATH.glob('*.md')}
    website_notes = {f.name: f for f in WEBSITE_NOTES_PATH.glob('*.md')}

    for name, temp_path in temp_obsidian_notes.items():
        website_path = WEBSITE_NOTES_PATH / name
        if name in website_notes:
            try:
                web_frontmatter, _ = _parse_markdown_file(website_path)
                obsi_f, obsidian_content = _parse_markdown_file(temp_path)
                web_frontmatter.update({k: v for k, v in obsi_f.items() if k in {'title'}})
                _save_markdown_file(website_path, web_frontmatter, obsidian_content)
            except Exception as e:
                print(f"Error updating {website_path}: {e}")
        else:
            # File missing in website - add it
            try:
                obsidian_frontmatter, content = _parse_markdown_file(temp_path)
                web_frontmatter = _create_web_frontmatter(obsidian_frontmatter, filename=name)
                _save_markdown_file(website_path, web_frontmatter, content)
            except Exception as e:
                print(f"Error adding {website_path}: {e}")

    for name, website_path in website_notes.items():
        if name not in temp_obsidian_notes:
            print(f"Warning: '{name}' exists in website notes but not in latest mirrored notes.")

    print("Review changes using the git diff in the website repo.")


def _extract_image_links(content: MdContent) -> list[str]:
    """Extracts image links from Markdown content."""
    image_pattern = re.compile(r'!\x5B\x5B([^\x5D]+\x5C.(?:jpg|jpeg|png|gif|webp))\x5D\x5D|!\x5B[^\x5D]*\x5D\x5C(([^)]+\x5C.(?:jpg|jpeg|png|gif|webp))\x5C))')
    links = []
    for match in image_pattern.finditer(content):
        link = match.group(1) or match.group(2)
        if link:
            links.append(link)
    return links


def _resolve_image_path(link: str, note_dir: Path) -> Path | None:
    """Resolves the absolute path of an image link."""
    path_link = Path(link)
    if path_link.is_absolute():
        if path_link.exists():
            return path_link
    else:
        # Try resolving relative to the note's directory
        potential_path = note_dir / path_link
        if potential_path.exists():
            return potential_path

        # Try resolving relative to the vault root
        potential_path = OBSIDIAN_VAULT_PATH / path_link
        if potential_path.exists():
            return potential_path

    # Fallback to searching the entire vault
    found_files = list(OBSIDIAN_VAULT_PATH.rglob(path_link.name))
    if found_files:
        if len(found_files) > 1:
            print(f"Warning: Found multiple images with name '{path_link.name}'. Using the first one: {found_files[0]}")
        return found_files[0]

    print(f"Warning: Could not find image '{link}'")
    return None


def _update_image_link_in_content(content: MdContent, old_link: str, new_link: str) -> MdContent:
    """Replaces an old image link with a new one in the content."""
    escaped_old_link = re.escape(old_link)
    pattern1 = re.compile(r'!\[\[' + escaped_old_link + r']]')  # Obsidian style
    pattern2 = re.compile(r'!\[.*?]\(' + escaped_old_link + r'\)')  # Markdown style (flexible alt)
    new_md_link = f"![]({new_link})"
    updated = pattern1.sub(new_md_link, content)
    updated = pattern2.sub(new_md_link, updated)
    return MdContent(updated)


def _clean_filename(filename: str) -> str:
    """
    Obsidian Files can contain spaces and special characters. Make them web compatible.
    Example: Converts "My Note (Test).md" to "my-note-test.md"
    """
    parts = filename.rsplit('.', 1)
    name_part = parts[0]
    extension = f".{parts[1]}" if len(parts) > 1 else ""
    cleaned = name_part.lower()
    umlaut_subs = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue'}
    for umlaut, sub in umlaut_subs.items():
        cleaned = cleaned.replace(umlaut, sub)
    cleaned = re.sub(r'[\s_(),]+', '-', cleaned)
    cleaned = re.sub(r'[^a-z0-9-]', '', cleaned)
    cleaned = re.sub(r'^-+|-+$', '', cleaned)
    cleaned = re.sub(r'-{2,}', '-', cleaned)
    return f"{cleaned}{extension}"


def _parse_markdown_file(file_path: Path) -> tuple[Frontmatter, MdContent]:
    """Parses YAML frontmatter and content from a Markdown file."""
    assert file_path.suffix == ".md"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw = f.read()
            if raw.startswith('---'):
                parts = raw.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    frontmatter = frontmatter if isinstance(frontmatter, dict) else {}
                    body = parts[2].strip()
                    return Frontmatter(frontmatter), MdContent(body)
    except yaml.YAMLError as e:
        print(f"Warning: Error parsing YAML in {file_path}: {e}")
    except Exception as e:
        print(f"Warning: Unexpected error reading {file_path}: {e}")
    return Frontmatter({}), MdContent("")


def _has_publish_tag(frontmatter: Frontmatter) -> bool:
    """Checks if the frontmatter contains the target publish tag."""
    tags = frontmatter.get(TARGET_YAML_KEY, [])
    if tags is None:
        return False
    if isinstance(tags, str):
        tags = [tags]
    return TARGET_TAG_VALUE in tags


def _create_web_frontmatter(obsidian_frontmatter: Frontmatter, filename: str) -> Frontmatter:
    return Frontmatter({
        'layout': 'note.njk',
        'title': obsidian_frontmatter.get('title', filename.replace("-", " ").title()),
        'tags': obsidian_frontmatter.get('tags', []),
        'btime': obsidian_frontmatter.get('btime'),
        'mtime': obsidian_frontmatter.get('mtime'),
        'status': obsidian_frontmatter.get('status', 'draft'),
        'permalink': "notes/{{ page.fileSlug }}/index.html",
    })


def _save_markdown_file(file_path: Path, frontmatter: Frontmatter, content: MdContent) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(dict(frontmatter), f, default_flow_style=False, allow_unicode=True)
        f.write('---\n')
        f.write(content)


if __name__ == "__main__":
    mirror_obsidian_notes()
    sync_notes()