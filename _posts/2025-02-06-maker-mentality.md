---
layout: post
title: A Maker's mentality - Solving my problems
date: 2025-02-06 14:08:42 +0100
tags: [reflections, personal]
excerpt: 
published: true
---
*Re-writing of an old LinkedIn / Twitter post*

As a machine learning person, I always dreamt to use ML and optimization to build tools that will improve my life and the life of others. 

However, ML models are useless artifacts on their own. Data analysis is probably more useful, giving insights and sometimes actionable items (e.g., my [French Journey series](www.placeholder.com)). The following obstacles were problematic:
1. Absence of data: a lot of the things that I want to optimize about my life require building data-collection tools and protocols, and of course, consistency in the data entry.
2. ML models / DA insights are useful when served and wrapped by the right software designs (and sometimes hardware) to make them come to life, and serve a purpose.

~5 years ago, I didn't have that much skills in tooling or building non-scientific software.

But this changes dramatically, thanks to advances in the tooling. 
1. Front-end: 
   1. I started with [Streamlit][streamlit-pkg], which made it possible to build interfaces to serve the value of the model to users and interact with them. Streamlit is great for simple interfaces, but once pushed too hard, you start to feel its limits.
   2. Last year, I added [Jinja2][jinja2-template], [HTMX][htmx], [TailwindCSS][tailwind] to the mix. This was a huge upgrade over Streamlit only: easier to customize and control. They do add substantially more complexity though, but it is controllable so far.
      1. Hopefully somewhere this year I will buildup more javascript capability as well.
2. DB and its management: 
   1. I used MongoDB for a while, mainly because of my familiarity with JSON format, and because of the convenient managed hosting services of [Mongo Atlas](https://www.mongodb.com/atlas).
   2. However, some painful experiences with MongoDB, while doing the HN analysis and some other personal projects (more on that in a later post) shifted me towards PostgresDB.
   3. Now, with [Supabase](https://supabase.com/), I get PostgresDB, authentication management, storage, with few clicks. This is much easier, and sufficient in most cases, and cheaper, than using AWS or GCP directly.
   4. And when there is a data-heavy application I am running, self-hosting the DB is the way to go.
3. Backend: Python + [Flask](https://flask.palletsprojects.com/en/stable/) 
4. Hosting and serving
   1. I host mainly on my Pi 4, 4-gb. If necessary, a cloud-based VM will do.
   2. Docker container and Docker-compose orchestrator
   3. Tunneling using Cloudflare and (and sometimes ngrok), which made it easy to expose my work.

I need to have the capability to solve my own problems and the problems of those around me. Gaining experience with these tools unlocks huge potentials. Now I can finally go to maker mode, and tinker with ideas. The motto of the day is: 

> See a need, fill a need 😊

<div class="tenor-gif-embed" data-postid="16449248377223966227" data-share-method="host" data-aspect-ratio="1.85185" data-width="100%"><a href="https://tenor.com/view/see-a-need-fill-a-need-robots-gif-16449248377223966227">See A Need Fill A Need Robots GIF</a>from <a href="https://tenor.com/search/see+a+need+fill+a+need-gifs">See A Need Fill A Need GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

[streamlit-pkg]: https://streamlit.io/
[htmx]: https://htmx.org/
[tailwind]: https://tailwindcss.com/
[jinja2-template]: https://jinja.palletsprojects.com/en/stable/