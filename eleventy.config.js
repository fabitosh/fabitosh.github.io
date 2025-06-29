import { feedPlugin } from "@11ty/eleventy-plugin-rss";

export default function (eleventyConfig) {
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
};
