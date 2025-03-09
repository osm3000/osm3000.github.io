---
layout: post
title:  "A view on France - Part 1"
date:   2022-02-16 00:00:00 +0200
tags: [projects]
categories: data-science machine-learning nlp
---

For whatever reason, even though I live in France for ~8 years now, I still struggle with learning French. My environment is always in English all the time, and all my French friends speak good English as well. To my surprise, speaking French is not a deal breaker as I once thought.

[All the code used in this analysis can be fine here](https://github.com/osm3000/Language-Analysis).

## Solutions that I tried

The road started normally, with dreams that working hard will do the trick, and that this problem is pretty much solved long time ago. Unfortunately, that proved to be not the case — for me at least. I tried:

- Apps like Babbel and Duolingo: Incredibly frustrating experience. Words that doesn’t seem to be used anywhere else. Whatever progress I make in the app (and trust me, I did a lot of progress) doesn’t seem to translate into reality at all. I don’t feel my comprehension or my ability to speak improved in any significant manner after few months of regular use of these apps. 
- Listening to TV series and programs: I just don’t like TV series or reality shows or any of that in general. It didn’t take long before I stopped this direction. 
- Listening to podcasts/videos on my favorite topics: mainly technical interests. That was quite helpful for sometime. It is a passive activity though.
- Community teachers: in platforms like [italki](https://www.italki.com/). A lot of progress were made there, but it is not easy to find enough good teachers or sustainable appointments. My objective was 1 hour of French everyday. No one teacher could satisfy this requirement. I ended up between 4~5 amazing teachers, but it is hard to coordinate and reserve the time. It was always a complex optimization problem.
- Courses in language centers: it was always incredibly expensive, hard to find on short notice, inflexible time slots that doesn’t fit with my work.

In short, no luck :( 

## Time for the technical hammer

My idea is to try to systematically understand what are the characteristics of the French language really is, and use that to design a data-driven curriculum for myself.

To understand the French language, I decided to analyze the articles in LeMonde newspaper. I scrapped a considerable amount of corpus, ~13K articles, from different domains. Using some basic NLP and frequency analyses, I am hoping to reach some insights about what the language is, that can enhance the quality of my decisions.

When analyzing the verbs, I decided to convert all the verbs to their original form (the simple present). Otherwise, it creates a lot of unnecessary clutter in the analysis.

## Overview on the results

[![](https://osm3000.files.wordpress.com/2022/02/wordcloud_allwords.png?w=1024)](https://osm3000.files.wordpress.com/2022/02/wordcloud_allwords.png)

Word-cloud for all the words

One can see that verbs like _avoir_, _etre_, and connectors like _qui_, _que_, _et_ and _il_ are the highest recurring words in the French language.

Let’s take a closer look at separate categories of those words: adverbs, verbs and nouns.

- ![](https://osm3000.files.wordpress.com/2022/02/wordcloud_alladverbs.png?w=1024)
    
- ![](https://osm3000.files.wordpress.com/2022/02/wordcloud_allverbs.png?w=1024)
    
- ![](https://osm3000.files.wordpress.com/2022/02/wordcloud_allnouns.png?w=1024)
    

My personal interest is to convert these words into flashcards, and based on their frequency and importance (I will tackle the _importance_ part later), I can focus on what really matter.

Although not a quantitative analysis, if you ever used tools like Babbel or Duolingo before, you might notice that there is an asymmetry between their words and those words. For example, on of the things you learn at the beginning in those applications are words like: garcon, fille, fils, pere, mere, ….etc, but you can notice that none of those words appears in those in big font in those word-clouds. 

### How many articles should I read?

Another issue of interest for me is: how many articles I do need to read in order to have been exposed to most of the words? I rephrased this problem in what I call the ‘insertion speed’: how much each article contribute with new unique words? 

The way I did it was not a comprehensive/realistic method in my opinion, but a fast and a quick lower-limit indicator. Basically, for each article, I measured how many words I didn’t see before, then add those new words to my seen-words-list, and move on to the next article, …etc. I ordered the resulting list — since it is noisy — in order to get a sense of what we are talking about.

[![](https://osm3000.files.wordpress.com/2022/02/insertionspeedordered.png?w=1024)](https://osm3000.files.wordpress.com/2022/02/insertionspeedordered.png)

One can see that, with around ~500 article, there is barely any new word added to the seen words. 

What I really like about the insertion speed is that it could be a way to manage my personal training procedure. If I’ve a system that is aware of the words I know so far (through articles I read, or manually inserted words), the system can then keep suggesting articles, in the area of interest, that either focus on older vocabulary (to enhance it), thus, having a small-to-no insertion speed, or to focus on learning new words, thus, asking the system for articles with higher insertion speed. 

This could be more beneficial, since it changes the personal training system from the sole focus on flashcards, to article-based learning (you will learn new words by reading the articles mentioning those words).

With a large enough repertoire of articles — and even an easy manner to add new articles — I can definitely imagine a pretty good training procedure.

#### Word Frequencies

What is really fascinating for me is the quantification of the long-tail phenomena in French (spoiler alert: MASSIVE long tail). To get an idea, let’s look at some numbers.

```
Total Number of words seen: ~7.6M words
Number of unique words: ~116K words
10% of the total words seen is just 3 unique words
20% of the total words seen is just 17 unique words
50% of the total words seen is just 375 unique words
80% of the total words seen is just 2624 unique words
90$ of the total words seen is just 6506 unique words
```

Even though the long-tail phenomena is expected, it is still mind-blowing for me to see it in action like this.

While aggregation is always amazing to get a good overview over the topic, it’s interesting to dive deeper and see more specific details. Let’s look at the same stats, but for verbs, nouns, and adverbs

Verbs

```
Total Number of words seen: ~1.2M verb
Number of unique words: ~11.5K verb
10% of the total verbs seen is just 3 unique verb
20% of the total verbs seen is just 14 unique verb
50% of the total verbs seen is just 139 unique verb
80% of the total verbs seen is just 585 unique verb
90% of the total verbs seen is just 1117 unique verb
```

Nouns

```
Total Number of words seen: ~2.8M noun
Number of unique words: ~41.6K noun
10% of the total verbs seen is just 27 unique noun
20% of the total verbs seen is just 77 unique noun
50% of the total verbs seen is just 408 unique noun
80% of the total verbs seen is just 1731 unique noun
90% of the total verbs seen is just 3599 unique noun
```

Adverbs

```
Total Number of words seen: ~604K adverb
Number of unique words: ~3.4K adverb
10% of the total verbs seen is just 0 !! unique adverb
20% of the total verbs seen is just 1 unique adverb
50% of the total verbs seen is just 11 unique adverb
80% of the total verbs seen is just 49 unique adverb
90% of the total verbs seen is just 94 unique adverb
```

All-in-all, assuming that being good at French is about mastering **80%** of the words, then I should focus on the **2624** words for the moment, over **2/3** of them are nouns and less than **1/3** are verbs. I can easily now transfer this into flash-cards, and dig into them :)

These are the links for those lists: [all words](https://github.com/osm3000/Language-Analysis/blob/main/results/noFilter/allWords.csv), [verbs](https://github.com/osm3000/Language-Analysis/blob/main/results/noFilter/allVerbs.csv), [nouns](https://github.com/osm3000/Language-Analysis/blob/main/results/noFilter/allNouns.csv) and [adverbs](https://github.com/osm3000/Language-Analysis/blob/main/results/noFilter/allAdverbs.csv). Maybe you can use them for your own application :)

## Origin of the data

I have built my database by scraping [_LeMonde_](https://www.lemonde.fr/) articles. After some investigation, I realized that the articles are organized in categories, in the form of 

```
https://www.lemonde.fr/<category>
```

The categories are so many, and it is not clear how to get a comprehensive list of them — or if that is the best approach. But, one can at least enumerate some of the interesting categories from the navigation bar. A better way would have been to parse the [archive of LeMonde](https://www.lemonde.fr/archives-du-monde/).

Within each article, you can look for the following tags in order to get the relevant information in the HTML source:

```
<description> : <tag type> - <class name>
Author name: span - author__name
Article description: p - article__desc
Article paragraphs: p - article__paragraph
Image links: figure > img - <No class name>
Image captions figure > figcaption - <No class name>
```

You should be able to scrap any article you like immediately with this info :)

To support the work of the journalists in LeMonde, I made a subscription in LeMonde. An added advantage is to get access to the full premium articles. Without a subscription however, using the same script, I can access the free part of the premium articles (almost 1/3 of the article).

## Conclusion

I started this little exercise out of frustration, and the more I dived into it, the more exciting it turned to be. As potential clear outcomes, one can now:

1. Make flashcards of the important words, and focus on them, based on the uni-gram/word frequency analysis.
2. Prepare an article/application based learning: if I can keep count of the insertion speed, and the current words that I know, and given that I've a repertoire of articles, the system can recommend me the next article to read, based on criteria in between the two extreme:
    1. I want to learn as many new words as possible (max insertion)
    2. I want to practice what I know only (min/zero insertion)
3. Analyze the quality of my writing:

But one can imagine even more applications here, for example:

1. Bi-gram/tri-gram analysis: time to focus on making sentences. Single words are interesting and all, but small repetitive pieces of sentences are much more powerful to learn. It will cut the thinking time considerably.
2. Importance analysis: with techniques like TF-IDF, what are the important words in French? so far, I focused on the common words only.
    1. Also perform this analysis per domain. It might help to ease the entry to specific domain (like science, technology, sport, ...etc) by getting the key words in that domain.
3. Cross this data with other data: one topic of interest for me is to understand the politicians and the media, and their inter-relationship. Recently, I got access to Twitter APIs. I would like to go deeper into what the french politicians talk about, their interaction, how and when a story breaks, ...etc.

I would love to know what you think :)
