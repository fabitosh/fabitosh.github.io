import { feedPlugin } from "@11ty/eleventy-plugin-rss";
import fg from "fast-glob";
import markdownIt from "markdown-it";
import { alertPlugin } from "markdown-it-github-alert";

const photographyImages = fg.sync(['photography/**/*.jpg', '!**/_site']);

export default function (eleventyConfig) {
    eleventyConfig.addCollection('notes', function (collectionApi) {
        return collectionApi.getFilteredByGlob('notes/*.md');
    });

    eleventyConfig.addCollection('photographyJpgs', function (collection) {return photographyImages});

    eleventyConfig.addPassthroughCopy("photography/800px/");
    eleventyConfig.addPassthroughCopy("css/");

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
        // Add Bootstrap classes to tables
        .use(function (md) {
            const defaultRender = md.renderer.rules.table_open || function (tokens, idx, options, env, self) {
                return self.renderToken(tokens, idx, options);
            };
            md.renderer.rules.table_open = function (tokens, idx, options, env, self) {
                return '<table class="table table-bordered table-hover">';
            };
        })
        // Github markdown callouts: note, tip, important, warning, caution
        .use(alertPlugin);
    eleventyConfig.setLibrary("md", md);
};
