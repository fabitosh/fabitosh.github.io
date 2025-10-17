---
btime: 2025-05-24 11:29
layout: note.njk
mtime: 2025-10-17
permalink: notes/{{ page.fileSlug }}/index.html
status: completed
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

RSS is a web feed technology that allows access to updates of online content in a standardized, computer-readable format and a core piece of my system.

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
- Do it yourself:
	- Select elements of the page to track changes from. If they change, create a new "post" in the feed. Solutions exist that use GitHub Actions.
- Reevaluate the importance. Is the information really worth the hassle?
- Check it using a supported way (Newsletter)

Few websites still show links to their RSS feeds directly in the UI. I was glad to find out, that we can get RSS feeds to youtube channels. 

## My Story
I have tackled this with two approaches so far.

### Readwise Reader 🔴
First, I have tried [Readwise Reader](https://readwise.io/read) for five months. They offer an elaborate information-stream aggregation through one channel. RSS-Feeds, Mail-Newsletters, pdfs, e-books etc. Which is what has drawn me to the platform. They also take care of ingesting non-RSS information channels.

In their Reader platform, there are feeds and a library. You can move feed-posts to the Library in "inbox", "later" or "archive" buckets. There is also a delete option hidden, but I don't think they want me to use it. Besides the three categories, the library is then divided into articles, books, emails, pdfs, tweets, videos and tags. One can build quite an elaborate system in there. But that was exactly my issue. It is *in there* - their proprietary cloud-platform. Yes, you can automatically extract your highlights/notes into Obsidian. But the reference material is archived in their system. Their data-export contains none of the structure we talked about above. Thus, I do not want to rely on it.

I have now moved away. I want it simpler.

### RSS Reader, Mail Newsletter, Obsidian Clipper 🟢
Not wanting to have all news through one single entry point simplifies things. Basically it comes down to handling information that is not supported by RSS feeds.

Checking more than one place is a trade-off I am happy to make. Even with Readwise, you are still checking mails and the instant messenger(s) at the very least.

My goal turns to get all relevant news through:
- RSS Feeds: Here I just want an aggregation of my curated feeds.
- Mail-Newsletters: For places without RSS feed, I will sign up with `mymail+newsletter@gmail.com` and create an inbox filter.
- If something does not offer neither, I'll bite the bullet and add it to a list of sites I want to infrequently and manually check.

News and articles I particularly liked and want to come back to, are to be stored as markdown on my machine.

#### RSS Reader
This brings us to the choice of the RSS Reader. 

Initial requirements:
- Must: No ads.
- Must: No forced "suggested articles" / no endless scrolling.
- Should: Somewhat modern design
- Must: Platforms: Works on my Android phone and Desktop. A usable browser-based implementation is fine.

The inbox should be small enough that I can process everything. Ultimately, the features can be limited.

Below are all candidates that would work for me.

Free and Open Source. Could be self hosted:
- [FreshRSS](https://freshrss.org/index.html)
- [Miniflux](https://miniflux.app/)
- [newsblur](https://newsblur.com/)

They can also be paired with phone apps, that interact with their corresponding APIs. One such platform is [ReadYou](https://github.com/ReadYouApp/ReadYou).

Proprietary candidates:
- [Inoreader](https://www.inoreader.com)
- [feeder](https://feeder.co/)

#### Archival
[Obsidian Web Clipper](https://obsidian.md/clipper) allows capturing web pages into markdown. It natively integrates with Obsidian. 
I might create a post about parts of my Obsidian setup another time. For the archival of my favorite articles, I make sure to include the following information into the frontmatter of the markdown:
- source
- author
- date when the website was captured
- date when the post has been created (if available)
- A tag, that clarifies it is clipped: `#clippings`
- A tag to specify I need to process it. `#to-process`
