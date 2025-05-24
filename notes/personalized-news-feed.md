---
btime: 2025-05-24 11:29
layout: note.njk
mtime: null
permalink: notes/{{ page.fileSlug }}/index.html
status: draft
tags:
- RSS
- apps
title: Personalized News Feed
---
I consider a news channel a one-directional information exchange to me.

Mine are cluttered and keeping up to date requires checking multiple platforms. Double annoying is, that some of those platforms are engineered to keep me on their platform beyond my intention.

This article summarizes my research on how to consolidate news channels into one place that:
- Is free of attempted addiction
- Lets me define the news feeds and how they are ordered

## RSS: Really Simple Syndication
A web feed technology that allows access to updates of online content in a standardized, computer-readable format.

> [!note]
> *Syndication*: The act of selling articles (newspaper, photography) to other organizations, so that they can be shown to a wider audience.
> *Web syndication*: Make content available from one website to other sites.

News publishers create an RSS feed (which itself is an XML file) listing their latest content with headlines, summaries, and links back to the full versions.

We then need an RSS reader to subscribe to those feeds, which pulls the latest changes on request. RSS gained widespread adoption in the early 2000s during the blogging boom. It is said to be the de facto standard for podcasts, blogs and news organizations.

### RSS Outlook and Challenges
Social Media has changed how a large percentage of people discover information. Some companies want to move away from it, as it tends to lead to less engagement. Which I, as a user, actually aim for.

If a site decides to not support RSS the following workarounds exist:
- Third-Party Services that generate them:
	- RSS.app - $8-$17/month
	- RSS Bridge: self-hosted FOSS
	- many more
- Do it yourself:
	- Select elements of the page to track changes from. If they change, create a new "post" in the feed. Solutions exist that use GitHub Actions.

I am curious how well that will work.

## Which Reader?
Initial requirements:
- Must: No ads.
- Must: No forced "suggested articles" / no endless scrolling.
- Should: Somewhat modern design
- Must: Platforms: Works on my Android phone and Desktop. Browser is fine.
- Some workflow to mark items as "read later" or directly add them to Obsidian Clipper.

I don't really need tags or folders. The inbox should be small enough that I see everything anyway. Ultimately, the features can be limited.
### Miniflux, self-hosted, FOSS
- Very minimalist
- Web only
- 15$/year if you do not want to self-host.

### FreshRSS, self-hosted, FOSS
- Powerful, highly customizable.

### Innoreader, proprietary
- Powerful and feature-rich.
- Free Tier
	- RSS feeds without ads.
	- Pull from newsletters is a paid feature
### Readwise Reader, Paid Platform aimed at power users
- Excellent platform support, highly polished.
- Aggregation Layer for Readwise, which aims to help organize read content (feeds, newsletters, kindle books, pdfs, etc. including notes made on them.
- Offers direct integration into Obsidian.

## Trying it out
Starting simple, I opted to try the free version of Innoreader and started setting up my RSS stream. Despite having this improved news funnel, I want to remain disciplined and subscribe to a small set of information that is highly useful to me. I still intend to learn mostly through books.

The process is not super seamless, but there are usually ways to get there. Some examples:
- [Anthropic News](https://www.anthropic.com/news): No official RSS feed found 🔴. The Github repo [Ohlshansk/rss-feeds](https://github.com/Olshansk/rss-feeds) came to the rescue.
- [paulgraham.com](https://www.paulgraham.com/articles.html): RSS Feed outdated since 2 years 🔴 The github repo mentioned above comes to the rescue again.
- [srf.ch](https://www.srf.ch/really-simple-syndication-rss-feeds-von-srf): Multiple maintained RSS Feeds ✅
- [Hungry Minds](https://www.hungryminds.dev/) Newsletter: Sends a weekly digest of articles. The RSS Feed does the same. I would have hoped to have individual articles within this framework. 🟧 I liked the format as Mail Newsletter (less spam), but prefer the granularity in the RSS. Might have to replace it with other sources.
- [Google Deepmind News](https://deepmind.google/discover/blog/): A bit tricky to find, but there is one: [Deepmind RSS](https://blog.google/technology/google-deepmind/rss/)
- youtube: Supports RSS feeds for each channel, but seemingly unofficially. The feed is: `https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID` The `CHANNEL_ID` can either be found in the URL or in the source code.
- [dcrainmaker.com](https://www.dcrainmaker.com/feed): Again, not found as link on the website but it exists as `/feed`.

### What I did not get to work within 5 minutes
- Private social media feeds
	- Instagram
	- Strava
- New Pumpfoil Gear from [Takoon](https://int.takoon.com/collections/pump-foil). They, like many other websites, offer a mail newsletter instead. The Newsletter Integration could come in handy.

## Initial Impression
After a somewhat cumbersome setup, I am loving the feed view. It's super cool to have infrequently updated personal blogs and youtube channels at one spot.

I am inclined to give Readwise Reader a try in the future but want to start out simple with Innoreader's free tier for now, aggregating and refining the feeds I need.