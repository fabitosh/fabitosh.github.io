import os
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

def _clean_filename(filename: str) -> str:
    """
    Obsidian Files can contain spaces and special characters. Make them web compatible.
    Example: Converts "My Note (Test).md" to "my-note-test.md"
    """
    name_part = filename.rsplit('.md', 1)[0]
    cleaned = name_part.lower()
    umlaut_subs = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue'}
    for umlaut, sub in umlaut_subs.items():
        cleaned = cleaned.replace(umlaut, sub)
    cleaned = re.sub(r'[\s_(),]+', '-', cleaned)  # Replace spaces/separators
    cleaned = re.sub(r'[^a-z0-9-]', '', cleaned)  # Remove invalid chars
    cleaned = re.sub(r'^-+|-+$', '', cleaned)     # Trim leading/trailing hyphens
    cleaned = re.sub(r'-{2,}', '-', cleaned)      # Remove consecutive hyphens
    return f"{cleaned}.md"

Frontmatter = NewType("Frontmatter", dict)
MdContent = NewType("MdContent", str)

def _parse_markdown_file(file_path: Path) -> (Frontmatter, MdContent):
    """Parses YAML frontmatter and content from a Markdown file."""
    assert file_path.suffix == ".md"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                parts = content.split('---')
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    frontmatter = frontmatter if isinstance(frontmatter, dict) else {}
                    content = "\n".join(parts[2::1]).strip()
                    return frontmatter, content
    except yaml.YAMLError as e:
        print(f"Warning: Error parsing YAML in {file_path}: {e}")
    except Exception as e:
        print(f"Warning: Unexpected error reading {file_path}: {e}")
    return {}, ""


def _has_publish_tag(frontmatter: Frontmatter) -> bool:
    """Checks if the frontmatter contains the target publish tag."""
    tags = frontmatter.get(TARGET_YAML_KEY, [])
    if tags is None:
        return False
    if isinstance(tags, str):
        tags = [tags]
    return TARGET_TAG_VALUE in tags

def mirror_obsidian_notes() -> None:
    """
    Finds notes with the publish tag in Obsidian vault,
    cleans their filenames, and copies them to the temp folder.
    """
    print(f"Starting mirror process...")
    print(f"Source Vault: {OBSIDIAN_VAULT_PATH}")
    print(f"Target Tag: '{TARGET_TAG_VALUE}'")
    print(f"Temp Folder: {TEMP_FOLDER_PATH}")

    if TEMP_FOLDER_PATH.exists():
        print(f"Clearing existing temp folder: {TEMP_FOLDER_PATH}")
        shutil.rmtree(TEMP_FOLDER_PATH)
    TEMP_FOLDER_PATH.mkdir(parents=True, exist_ok=True)

    copied_count = 0
    for item in OBSIDIAN_VAULT_PATH.rglob('*.md'):
        if OBSIDIAN_TRASH_FOLDER_NAME in item.parents:
            continue
        if item.is_file():
            obsidian_frontmatter, _ = _parse_markdown_file(item)
            if _has_publish_tag(obsidian_frontmatter):
                web_name = _clean_filename(item.name)
                target_path = TEMP_FOLDER_PATH / web_name
                try:
                    shutil.copy2(item, target_path) # copy2 preserves metadata like modification time
                    copied_count += 1
                except Exception as e:
                    print(f"Error copying {item} to {target_path}: {e}")
    print(f"Mirroring complete. Copied {copied_count} notes to {TEMP_FOLDER_PATH}")

def _create_web_frontmatter(obsidian_frontmatter: Frontmatter, filename: str) -> Frontmatter:
    return Frontmatter({
        'layout': 'note.njk',
        'title': obsidian_frontmatter.get('title', filename.replace("-", " ").title()),
        'tags': obsidian_frontmatter.get('tags', []),
        'btime': obsidian_frontmatter.get('btime'),
        'mtime': obsidian_frontmatter.get('mtime'),
        'status': obsidian_frontmatter.get('status', 'draft'), # scribble, draft, completed, revision
        'permalink': "notes/{{ page.fileSlug }}/index.html",
    })


def _save_markdown_file(file_path: Path, frontmatter: Frontmatter, content: MdContent) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(dict(frontmatter), f, default_flow_style=False, allow_unicode=True)
        f.write('---\n')
        f.write(content)


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
                web_frontmatter.update({k:v for k, v in obsi_f.items() if k in {'btime', 'mtime'}})
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


if __name__ == "__main__":
    mirror_obsidian_notes()
    # sync_notes()
