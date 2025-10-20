# Package init for obsidian_sync helpers

import pytest

from obsidian_sync.mirror import _extract_image_links, MdContent

# Consolidated parametrized tests for image link extraction regex
# Merged from former test.py and test_image_links.py
@pytest.mark.parametrize(
    "content, expected",
    [
        ("![[Image.PNG]]", ["Image.PNG"]),
        ("Some text before ![[My Image.PNG]] and after", ["My Image.PNG"]),
        ("Before ![[Folder With Spaces/Image Name.PnG]] after", ["Folder With Spaces/Image Name.PnG"]),
        ("![[path/to/Fancy Photo.JpEg]]", ["path/to/Fancy Photo.JpEg"]),
        ("![alt](path/to/photo.jpeg)", ["path/to/photo.jpeg"]),
        ("![](pic.GIF)", ["pic.GIF"]),
        ("![ ](pic.webp)", ["pic.webp"]),
        ("![one](a/b/c.webp) text ![[Second.JPG]] and ![two](x.PNG)", ["a/b/c.webp", "Second.JPG", "x.PNG"]),
        ("![first](a/b/c1.gif) text ![[Second Image.PNG]] more ![third](third.jpeg)", ["a/b/c1.gif", "Second Image.PNG", "third.jpeg"]),
        ("![[UPPERCASE.JPEG]]", ["UPPERCASE.JPEG"]),
        ("![alt](complex.name.v1.final.png)", ["complex.name.v1.final.png"]),
        ("![capture](folder/name.with.dots.image.jpeg) trailing", ["folder/name.with.dots.image.jpeg"]),
        ("![[2024-06_report_final-V2.Gif]]", ["2024-06_report_final-V2.Gif"]),
        ("![[dup.png]] text ![[dup.png]] ![alt](dup.png)", ["dup.png", "dup.png", "dup.png"]),
        ("![stuff [inner]](inner.webp)", ["inner.webp"]),
        ("![alt [inner] text](folder/pic.gif)", ["folder/pic.gif"]),
        ("See ![img](valid.jpg) and [ref](doc.md) plus ![[Another.WEBP]]", ["valid.jpg", "Another.WEBP"]),
        ("![both](folder/photo.jpg?debug#area)", ["folder/photo.jpg?debug#area"]),
        ("![[Embed Image.PNG#zone]] and ![[Other.jpeg?cache=true]]", ["Embed Image.PNG#zone", "Other.jpeg?cache=true"]),
        ("![[Folder/Image.PNG?cache=false]]", ["Folder/Image.PNG?cache=false"]),
        ("![[Folder/Sub/Image.GIF#hash]]", ["Folder/Sub/Image.GIF#hash"]),
        ("![mix](Folder Name/Image One.png?ver=2)", ["Folder Name/Image One.png?ver=2"]),
        ("![spaced](Folder Name/Another Image 01.png)", ["Folder Name/Another Image 01.png"]),
        ("![q](img/photo.jpeg?version=3)", ["img/photo.jpeg?version=3"]),
        ("![frag](img/diagram.PNG#section-one)", ["img/diagram.PNG#section-one"]),
    ],
)
def test_extract_image_links(content: str, expected: list[str]):
    assert _extract_image_links(MdContent(content)) == expected

@pytest.mark.parametrize(
    "content",
    [
        "![broken](image.svg)",          # unsupported extension
        "![[broken.svg]]",               # unsupported extension obsidian
        "![[missing.png",                # missing closing brackets
        "![alt](missing.jpg",            # missing closing parenthesis
        "![alt]missing.jpg)",            # malformed markdown
        "![[noext]]",                    # no extension
        "![wrong](picture.bmp?x=1)",     # unsupported bmp extension with query
        "![wrong](image.svg?x=1)",       # unsupported svg extension with query
        "![[Some.svg#frag]]",            # unsupported svg extension with fragment
    ],
)
def test_extract_image_links_negative(content: str):
    assert _extract_image_links(MdContent(content)) == []
