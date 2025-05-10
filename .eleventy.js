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
    // Add Bootstrap classes to blockquotes
    .use(function(md) {
        const defaultRender = md.renderer.rules.blockquote_open || function(tokens, idx, options, env, self) {
            return self.renderToken(tokens, idx, options);
        };
        md.renderer.rules.blockquote_open = function(tokens, idx, options, env, self) {
            return '<blockquote class="blockquote border-start border-4 ps-3">';
        };
    })
    // Add callout support (e.g. > [!note] ...)
    .use(markdownItContainer, 'callout', {
        validate: function(params) {
            return params.trim().match(/^\[!(note|info|warning|tip)\]/i);
        },
        render: function(tokens, idx) {
            const m = tokens[idx].info.trim().match(/^\[!(note|info|warning|tip)\]/i);
            if (tokens[idx].nesting === 1) {
                // opening tag
                let type = m[1].toLowerCase();
                let alertClass = {
                    note: 'alert-primary',
                    info: 'alert-info',
                    warning: 'alert-warning',
                    tip: 'alert-success'
                }[type] || 'alert-secondary';
                return `<div class="alert ${alertClass} callout mb-2">`;
            } else {
                // closing tag
                return '</div>';
            }
        }
    });
        // github markdown callouts: note, tip, important, warning, caution
        .use(alertPlugin);
    eleventyConfig.setLibrary("md", md);
};