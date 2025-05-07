---
btime: 2024-04-12
layout: note.njk
mtime: 
permalink: notes/{{ page.fileSlug }}/index.html
status: scribble
tags:
- developer
title: Creating Websites
---
My aim is to create websites as a platform with minimal mingling in the web languages. The use case determines the required framework. This is a beginners ramble overview.

## Display Static Content

Here, I want to have files that can be visualized directly on any browser without relying on any environment setup. Each
consumer should see a mostly identical output.
Those sites are lean, secure, and generally simple. In the past, I have not overly enjoyed creating and maintaining
such sites, which was the reason for me looking into it.
My goal is to set the page up once and from then on only worry about the content anymore.

### Painpoint: Repetitive code

The subpages will contain repetitive code, such as the header or navigation. To avoid the need to adjust all files when
changing one of those elements, a static site generator comes in handy.
[Eleventy](https://www.11ty.dev/) lets us create templates and generates the final static webpage with all its
html-files.

### Painpoint: HTML

When writing my mind, I don't do that directly as HTML. Eleventy allows us to have markdown files as raw, content input
for our webpages.

### Painpoint: CSS/JavaScript

Placing all the individual boxes of a website in the right place for multiple browsers, and screen resolutions and
keeping it up to date with the latest developments can quickly start consuming time.
[Bootstrap](https://getbootstrap.com/) massively simplifies this by offering dynamic design templates. [Tailwind CSS](https://tailwindcss.com/) is said to be a more modern replacement.

### npm

We have identified two packages that help us resolve most of the pain points.
[npm](https://www.npmjs.com/) manages packages for JavaScript/node.js similarly to the way `poetry` or `setuptools` do
for Python projects.
The dependencies are stored in `package.json`. To create the dependencies run

```bash
npm init -y
npm install @11ty/eleventy --save-dev
```

Generate HTML files

```bash
npx @11ty/eleventy
```

Start up a local web server that hot-reloads the page

```bash
npx @11ty/eleventy --serve
```

### Deployment

As the website is fully static, it can be hosted anywhere.

This website is the result of this evaluation. Feel free to check out
its [source code on github](https://github.com/fabitosh/fabitosh.github.io). I automatically deploy this site on any push to master.

## Dynamic Websites

Next: Plotly Dash, host a plotly dash app (chat analyzer) on a subdomain?