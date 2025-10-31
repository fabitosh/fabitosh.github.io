import {feedPlugin} from "@11ty/eleventy-plugin-rss";
import fg from "fast-glob";
import Shiki from '@shikijs/markdown-it'
import markdownIt from "markdown-it";
import {alertPlugin} from "markdown-it-github-alert";

const photographyImages = fg.sync(['assets/photography/**/*.jpg', '!**/_site']);

export default async function (eleventyConfig) {
    eleventyConfig.addCollection('notes', function (collectionApi) {
        const notes = collectionApi.getFilteredByGlob('notes/*.md');
        // latest changes first
        notes.sort((a, b) => {
            const dateA = a.data.mtime || a.data.btime;
            const dateB = b.data.mtime || b.data.btime;
            return new Date(dateB) - new Date(dateA);
        });
        return notes;
    });

    eleventyConfig.addCollection('photographyJpgs', function () {
        return photographyImages
    });

    eleventyConfig.addPassthroughCopy("assets/");

    eleventyConfig.addShortcode("githubIcon", function() {
        return `<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
</svg>`;
    });

    eleventyConfig.addPlugin(feedPlugin, {
        type: "rss",
        outputPath: "/feed.xml",
        collection: {
            name: "notes",
            limit: 10,
        },
        metadata: {
            language: "en",
            title: "fabio.earth – Notes",
            subtitle: "Exploring technology and curiosity.",
            base: "https://fabio.earth/",
            author: {
                name: "Fabio Meier",
            },
            copyright: "Copyright © 2025 Fabio Meier",
            generator: "Eleventy + @11ty/eleventy-plugin-rss"
        }
    });


    let md = markdownIt({
        html: true,
        // breaks: true,
        linkify: true
    })
        // Github markdown callouts: note, tip, important, warning, caution
        .use(alertPlugin)
        // Syntax highlighting of code blocks
        .use(await Shiki({
            themes: {
                light: 'catppuccin-latte',
                dark: 'catppuccin-mocha',
            },
            defaultColor: 'light-dark()',
        }));
    eleventyConfig.setLibrary("md", md);
};
