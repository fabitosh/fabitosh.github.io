const fg = require("fast-glob");
const { alertPlugin } = require("markdown-it-github-alert");
photographyImages = fg.sync(['photography/**/*.jpg', '!**/_site']);
module.exports = function(eleventyConfig) {
    eleventyConfig.addCollection('notes', function(collectionApi) {
        return collectionApi.getFilteredByGlob('notes/*.md');
    });
    eleventyConfig.addPassthroughCopy("photography/800px/");
    eleventyConfig.addPassthroughCopy("css/");
    eleventyConfig.addCollection('photographyJpgs', function(collection) { return photographyImages});

    let markdownIt = require("markdown-it");
    let md = markdownIt({
        html: true,
        breaks: true,
        linkify: true
    })
        // Add Bootstrap classes to tables
        .use(function(md) {
            const defaultRender = md.renderer.rules.table_open || function(tokens, idx, options, env, self) {
                return self.renderToken(tokens, idx, options);
            };
            md.renderer.rules.table_open = function(tokens, idx, options, env, self) {
                return '<table class="table table-bordered table-hover">';
            };
        })
        // github markdown callouts: note, tip, important, warning, caution
        .use(alertPlugin);
    eleventyConfig.setLibrary("md", md);
};