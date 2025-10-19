import { feedPlugin } from "@11ty/eleventy-plugin-rss";
import fg from "fast-glob";
import markdownIt from "markdown-it";
import { alertPlugin } from "markdown-it-github-alert";

const photographyImages = fg.sync(['photography/**/*.jpg', '!**/_site']);

export default function (eleventyConfig) {
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

    eleventyConfig.addCollection('photographyJpgs', function () {return photographyImages});

    eleventyConfig.addPassthroughCopy("photography/800px/");
    eleventyConfig.addPassthroughCopy("css/");
    eleventyConfig.addPassthroughCopy("assets/js/**.js");

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
        .use(alertPlugin);
    eleventyConfig.setLibrary("md", md);
};
