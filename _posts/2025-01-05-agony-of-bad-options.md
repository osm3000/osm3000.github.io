---
layout: page
title:  "Escaping from Jekyll...back to Jekyll"
date:   2025-01-05 00:00:00 +0100
published: true
---
*Updated: 02/04/2025*


I wanted to have: 
1. A fast WYSIWYG editor for my static website
2. A decent capability to have a nice theme. I feel it is not a lot to ask.
3. Go a bit beyond Markdown in text formatting: is it too much to wish for a couple of images side by side? Or captioning an image? Or just create a table without the dash maze of markdown, or without going through another website?
4. Go beyond the blog linear structure.
5. Have an OpenAI integrated with it, since I am relying on it more and more now for proofreading. And I want to use my OpenAI account, or my GitHub Copilot account (I don't see the point of paying for another account).

I just wanted to have an environment to focus on writing and my projects.

I've tried to find a stack that works with my current Jekyll-based website, but to no avail. I don't want to edit Jinja templates and CSS. Sometimes, simple things are difficult (like where is the CSS of my current theme?).

So, I went shopping for a new platform. 

Changing platforms is the most unproductive and painful activity one can do. There is really no winning here, just losses. Instead of investing time in doing what I am supposed to do, I end up exporting and importing content, just to discover a catch somewhere. It is exhausting and draining.

## Platforms I've tried

### WordPress
My first website was in WordPress, and it has a special sentimental value to me.

The WordPress editor, however, was too slow as the article got larger. Writing [the Chernobyl article](https://osm3000.wordpress.com/2023/01/06/hbo-chernobyl-v2/) was a painful memory. There is something unnatural about clicking the keyboard button and waiting for the letter to emerge. It is the reason for my insistence on having a local editor. I found local WordPress editors, which felt great, until I was hit with reality: I need to pay for the business plan in order to connect to my existing website.

A big mistake that I made back then was that I wasn't thinking about owning the domain. Now, binding my domain is pricey, and it feels that there are hidden costs that are yet to come.

1. Depending on the length of the article, the editor can be very slow.
2. I am not sure about the themes.
3. Nicer experience than writing in Markdown directly.
4. Still centered around a blog structure.
5. No AI integration (maybe via a plugin).

### Notion
I love Notion. I think it is the right concept and it is on the right track. When using it locally, it is fantastic. My eyes feel comfortable looking at it.

So, I created a demo site, with a few pages, to get a sense of it. 

A Notion site is too slow for a website. It doesn't get the concept of a static website. The homepage, sometimes, took ~20 seconds to load. If the content grows a bit more, then I would feel more nervous about the whole thing.

It is also pricey: If I pay yearly, it is ~12 euros/month to bind my domain to it. And most probably it will cost even more with some extra features, like Notion AI.

1. The editor is pretty good.
2. Much fewer options for the themes.
3. Definitely way beyond Markdown.
4. Much more flexible than a blog structure.
5. I liked the AI integration feature: helpful for proofreading.

### Obsidian 
Obsidian provides a good compromise at the moment: if required, I can still go inside the HTML and CSS, but otherwise, I don't need to think about it too much.

I was particularly excited about the canvas feature. Imagine creating some pages using it, that would be awesome!

I tried to get a sense of how an Obsidian website will look, but I couldn't find a way to preview it locally. So, I paid for Obsidian Site.

Pretty quickly, I realized that I can't publish an Obsidian Canvas. That was a bummer, but not a deal breaker. But it highlights the risk of migrating to new platforms: there are always issues that will emerge that are hard to foresee beforehand.

1. A local editor, decent and fast.
2. Fewer options for the themes.
3. It is a step beyond Markdown.
4. It goes a bit beyond the blog structure.
5. There is no AI integration (probably I need to install a plugin).

### Substack
By now, I am traumatized by the speed of web editors. The WordPress experience left scars. Although I tried the Substack editor a few times, and I've not found an issue, I still can't trust it fully. But, after a lot of thinking and tinkering, I decided it was time to grow up and [migrate to Substack](https://omar3000.substack.com/). I liked the idea of having subscribers as well.

I liked the idea of a one-time payment to bind my domain to Substack. It is a bit pricey though (~50 $), and I don't get the logic for this. If it was about the editor, hosting fees, or the subscription option, they would have charged upfront to use Substack. It feels that they want to lock people in for a future purpose.

While copy-pasting my previous work, I was shocked to realize that I can't make tables using the editor (I have to rely on another website, and embed the generated table in Substack), but interestingly, someone thought that creating financial charts is more important to have in the editor.

![Substack financial charts](/assets/images/bad_choices/substack_financial_charts.png)

Again, the whole experience highlights all these unpleasant surprises arising from migrating platforms.

1. A web editor, decent. While I've not encountered a problem with speed yet, the absence of tables was just incomprehensible to me.
2. Very limited theme options.
3. It is a step beyond Markdown.
4. Constrained to the basic blog structure.
5. There is no AI integration.

## Back to Jekyll and GitHub
I still feel my initial demands were reasonable, yet I couldn't find a solution.

The unfortunate conclusion was that I can only trust the web standards, not company statements. 

The current business practices make me doubtful of almost any company. The advertised price is rarely the price you actually pay, and the highlighted advantage is usually a smokescreen to hide the catch. And there is always a catch. A savvy company would delay the discovery of the catch until you are too deep, that it will be hard to escape.

I am suspicious about raising the slogan that "you own the content": Content has no value if it is not discoverable, and discoverability is tied to the domain. One way to lock you in is to promote that "you own the content", but the catch is your domain. You would pay a lot to bind the domain.

There is a strong stigma against building things from scratch, and I agree with it to a certain extent. I've been down this road many times, and I do wonder if it was worth it sometimes. But it feels more and more that I can rely only on the old players, or rely on myself. The new players are rarely trustworthy.

So, back to Jekyll. I took a course on CSS and HTML, and I tried my best with the site. I feel better about it now than earlier when I started this. I will improve it gradually. I also need to accept the mentality that markdown on VSCode is good, and if it falls short in some places, I will use HTML and CSS instead.

This will not be very sustainable however as the blog grows. I think I will need to build a custom solution at a certain point (thinking Flask, Jinja, maybe HTMX?, Tailwind, S3). But I will worry about this later.