const fg = require("fast-glob");

photographyImages = fg.sync(['photography/**/*.jpg', '!**/_site']);

module.exports = function(eleventyConfig) {
    eleventyConfig.addCollection('notes', function(collectionApi) {
        return collectionApi.getFilteredByGlob('notes/*.md');
    });

    eleventyConfig.addPassthroughCopy("photography/800px/");
    eleventyConfig.addCollection('photographyJpgs', function(collection) {
        return photographyImages});
};