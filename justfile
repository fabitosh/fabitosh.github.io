# List available recipes
default:
    @just --list

# Install node dependencies
install:
    npm install

# Serve the site with live reload at http://localhost:8080
serve:
    npm run serve

# Build the site into _site (same as CI)
build:
    npm run build

# Mirror notes tagged tech/website/hosted from the Obsidian vault into notes/
sync:
    cd obsidian_sync && uv run mirror.py

# Run the obsidian_sync tests
test:
    uv run --project obsidian_sync pytest obsidian_sync

# Remove build output and sync temp files
clean:
    rm -rf _site obsidian_sync/_tmp
