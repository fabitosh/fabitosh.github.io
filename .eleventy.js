const fg = require("fast-glob");

photographyImages = fg.sync(['pages/photography/**/*.jpg', '!**/_site']);

module.exports = function(eleventyConfig) {
    eleventyConfig.addCollection('notes', function(collectionApi) {
        return collectionApi.getFilteredByGlob('pages/notes/*.md');
    });

    eleventyConfig.addPassthroughCopy("pages/photography/800px/");
    eleventyConfig.addCollection('photographyJpgs', function(collection) {
        return photographyImages});
};