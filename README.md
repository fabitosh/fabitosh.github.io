# fabitosh.github.io

Personal site built with [Eleventy](https://www.11ty.dev/).

## Local development

```sh
npm install
npm run serve   # eleventy --serve, live at http://localhost:8080
```

## Publishing

Pushing to `main` triggers a GitHub Actions build that deploys to GitHub Pages automatically.

## Obsidian sync

Notes are authored in an Obsidian vault, not here directly. [`obsidian_sync/`](obsidian_sync/) holds a Python script that mirrors vault notes tagged `tech/website/hosted` into this repo (cleaning filenames and copying referenced images):

```sh
cd obsidian_sync && uv run mirror.py
```

See [obsidian_sync/README.md](obsidian_sync/README.md) for details.
