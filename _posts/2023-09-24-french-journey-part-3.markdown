---
layout: post
title:  "French Journey - Part 3"
date:   2023-09-24 00:00:00 +0200
categories: thinking
---

- [Part 1](http://osm3000.wordpress.com/2022/02/16/a-view-on-france-part-1/)

- [Part 2](http://osm3000.wordpress.com/2022/08/19/a-view-on-france-part-2-data-driven-estimation-to-learn-french/)

This whole journey started out for very different objectives (analyzing the political scene in France), and then it progressed forward, out of curiosity.

In parts [1](https://osm3000.wordpress.com/2022/02/16/a-view-on-france-part-1/) and [2](https://osm3000.wordpress.com/2022/08/19/a-view-on-france-part-2-data-driven-estimation-to-learn-french/), I presented preliminary results of the results of the analysis of nearly 1.5 million articles from [LeMonde](http://www.lemonde.fr), and _I extracted the most frequently used 80% of French words, which was nearly 2600 words_. I came to realize that it might be useful to solve my problem in learning French.

The main difficulty in such situations is to design a process to distill these desires and assets into clear requirements, using available tools, to produce actionable habits. This is often a non-linear phase. After that comes the assembly part: acquire (or build) all these pieces and put them together. Then, reality check: let’s use it for a while. Iterating (minor or major) is the name of the game: the faster, the better. And through all of this, there is a deep imposter syndrome and flying demons everywhere.

To learn French using my previous findings, my initial thoughts were:

1. Memorize the single words using flashcards

3. Learn in context:
    1. (Passive) Reading: I unleashed an optimization system to find the best set of articles from LeMonde, which allowed me to see every word in context at least 10 times. This mounted to 400 articles.
    
    3. (Active) Writing: Similar to reading, the objective was to deliberately write sentences/paragraphs that will lead to ~10 times repetition of each word.

This article is to describe my experience so far. Once all the pieces were in place, I gave myself 2 months to try it all on daily bases.

Before we start, it is important to give on the context on why my motives, and the challenges I faced that drove me there:

1. I would love to learn French
    1. To get better at integrating with the society
    
    3. Out of sheer curiosity: to unlock this massive culture
    
    5. Being accustomed to ignorance is contagious to other aspects of life

3. Despite many attempts, I could not find a suitable course: either it was too expensive, course hours are inconvenient (in the middle of the working hours), or unsuitable medium (I really didn’t like courses over zoom).
    1. With no course, there is no curriculum / gradual steps
        1. French people don’t make it any easier. The majority of people I interact with speaks very well English, and people will switch to English if they feel you are hesitating or misspelling.

5. I don’t have a natural stress to learn French
    1. My work was / is / likely will be in English.
    
    3. All my French friends speak perfect English.
    
    5. A lot of French people speak English just fine.

7. I don’t watch TV, which is ironic: I thought that was a superior habit, but in this case, it is a massive weakness.

Simply speaking: It's a matter of numbers, and I don’t have the proper context to do the numbers.

# Experience

## Words

I formatted and uploaded all the extracted words and their translations to [Anki](https://apps.ankiweb.net/), a powerful flashcard app. The results were immediate, tangible, and amazing!

At the beginning, I started with learning 100 new words a day, and reviewing 200 more (since I already know many words). As I progressed (after ~700 new words), the rhythm changed to 50 new words and review about 100.

There has been a direct improvement in my conversation and reading skills.

- I am able to use a wider range of vocabulary to express myself and my point of view. When I am stuck, I have a larger toolbox to choose from.

The transition from extracted words to flashcards was "almost" seamless:

1. One-to-one translation between French and English was sometimes NOT capturing the meaning.
    1. Many French words map to the same English word, but if you look at the French dictionary, there can be subtle or important differences in meaning.
        1. This required cleaning, consolidation of words, and compromises.
        
        3. This required some time to iron, and I don't think the resolution was perfect.
        
        5. This point provided clear evidence for the need for more context (phrases / paragraphs).

3. A few entities (such as some people's names) have escaped my processing pipeline, which further required cleaning.

After cleaning, approximately 400 words were removed from my word list.

Certain words, such as propositional letters, were challenging to learn and still are. This indicates that a larger context, such as a phrase, may aid in the learning process of these words. More context and modalities (using them in writing, during hearing, …etc) and special focus on them is required.

# Next steps

## Words and Reading

The next frontier is to solidify these words with reading and writing. For the reading part, a friend tried generating example phrases using ChatGPT for the new words he is learning in german. Naturally, I wanted to try the same.

With simple prompts, I was able to:

1. Extract the new words from any text

3. Generate 3 example phrases for any word I want, and their translations.
    1. If the word is a verb, then generate 3 phrases for each tense (upping the game now).

And then it was easy to parse the words and sentences, and add them to Anki as flashcards.

The idea is to generate a replacement for the LeMonde articles, while maintaining the objective of being focused. In other words, I wanted to generate the **_minimum viable book for the learning french language_**.

I have just built the pipeline to do so, and generated the flashcards. You can find:

- [A website I created so you can try that yourself](https://dashboard.osm-ai.net/)

- [The Github for the package with more tools to build your own flashcards](https://github.com/osm3000/LangLearnCopilot)

The Anki words will continue to be part of my practice, with incremental increase of new words that I encounter. There are already many new words in the phrases generated by GPT 😄

An alternative plan would be to use such a system for problematic words only (e.g., I am struggling with proposition letters, thus, it makes more sense to have a concentrated reading examples), while investing more in reading books. To be tried.

## Writing

One of the annoyances I found out about this is to have track what I am writing, and enforce certain objectives.

For example, a process I’ve in mind is to have a list of X words daily, and I need to use them in a writing assignment of 100 words. The objective, similar to flashcards, is to hit each word 10 times at least.

A proxy for proper correction (to be investigated) is to use GPT model at the end to generate a correction for my writing, and use this as the ground truth for what I’ve truly practiced.

I will release this app later when it is ready.

# Final note

This whole project was fun. I learned a lot of new things, and came to appreciate my own limitations on many other things (I will probably write about this separately).

- It is a design problem: Finding the right design to unlock the right functionality. While my design skills are not great, I found the hard way that my execution capacity is not adequate my dreams (my tech stack is geared more towards machine learning, research and backend). This was a motive to improve my design and technical skills.

- There is a deep value in having a progress bar and metrics to track my progress, even if they are noisy.  
    Better still, it is nice to have the "one number" that summarize your progress. After that, you can have other numbers that shed light on different aspects of that progress.

- While practice and perseverance are the key, and I am already enjoying the mix of road building and exploration that I am doing, I think a key item is to find a manageable objective: Speaking french fluently (my objective since long) is unrealistic in the absence of full immersion, and immersion will not happen without a need or a stress, interior or exterior.  
    But a limited immersion seems feasible (and personally interesting):
    - Reading: I love magazines (space, cars, tech), history, and eager to explore literature (Jules Verne in French? Let’s go!).
    
    - Watching / Listening: I like documentaries in different subjects ([ARTE](https://www.arte.tv) come to mind).
    
    - Writing small nuggets daily (~100 words or so), maybe focusing on using certain words, seems doable.

- Speaking is still a challenge, but my hypothesis is: if I managed the other three, then when the opportunity comes to immerse, I will be better prepared.

To be continued...
