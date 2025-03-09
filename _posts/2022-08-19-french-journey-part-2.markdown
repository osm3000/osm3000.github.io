---
layout: post
title:  "A view on France - Part 2"
date:   2022-08-19 00:00:00 +0200
tags: [projects]
categories: data-science machine-learning nlp
---

Following on my journey to explore the French language (check [part 1](https://osm3000.wordpress.com/2022/02/16/a-view-on-france-part-1/)), in this part I wanted to better understand how to many articles do I need to read randomly from LeMonde in order to reach my learning objectives, and if there is a way to guide this process (instead of just random articles). The code for the [simulation is here](https://github.com/osm3000/Language-Analysis/blob/dirty_experiment/heavy_exp.py), the analysis is [available here](https://github.com/osm3000/Language-Analysis/blob/dirty_experiment/number_of_articles_to_master_french.ipynb).

# Boring background

A question that always fascinated me to quantify the learning of a new language.

1. How to represent the 'learning process' in an objective way?
2. How much effort is required to reach this objective?
3. Can I optimize my efforts in order to achieve higher efficiency?

Beside curiosity, the motivation from this analysis is pave the way building a learning system for myself, that can monitor my training and progress, and optimize my learning trajectory.

Of course, it can be argued that maybe it is better to spend the time in actually learning French than analyzing it. There are two points here:

1. Despite huge efforts to learn French (and to some extent I can speak and comprehend what people are saying at the moment), the gains have been low. Believe it or not, in academia and a lot of tech companies nowadays, there is no natural need/urgency to speak French! And everyone speaks English.
2. I like to understand how things work from first principles point of view.
3. I realize more and more that, even in English, my vocabulary is becoming more and more limited. Being in France, speaking English with people from many nationalities, you end up mastering what's called "international English" and build a habit for using simpler, limited set of vocabulary.

Vocabulary are the building blocks for thinking. It represents the ability to abstract concepts and ideas, thus, it allows me to remove the clutter, and see connections and relations that were not obvious before.  
Thus, aside from French, I would like to use such a system for English as well, to maintain or expand or my skills.

While I am focusing on _reading articles from LeMonde_ as the only way to learn, which is unrealistic for sure, it is a start. One can imagine combining this data from other streams of data (which I will do), like Twitter, Reddit, Podcast/Video transcripts, ....etc.

Plus, most importantly, I fucking love numbers :D

# Assumptions

It is important to consider the simplifications and assumptions made here in this analysis

1. I am assuming that learning French = learning 80% of the most common French vocabulary. This is ~2600 words. To understand how I got those words, check [part 1](https://osm3000.wordpress.com/2022/02/16/a-view-on-france-part-1/).
    1. The previous analysis was done on a small sample of articles, mostly from the recent couple of years. I have redone this calculation from scratch for the 1 million LeMonde articles used in this new analysis, and concluded that 80% of the French language is ~3500 words.
2. "Learning those words" translates to: seeing each word at least 10 times.
3. Every 100 articles, I model "memory loss": for each word of the target vocabulary that I didn't see in the last 100 articles, I will reduce its score by 1 point (If you don't practice, you will forget).
4. While it is simplified to translate learning French to learning 80% of the words, and it is focused only on the "reading" part, and it might be criticized as language is more than just words, I would argue that it can be an _okay_ proxy:
    1. You are not learning the words in isolation here, that is the beauty of learning by reading articles.
    2. The more you articles, the more likely that you will see different combinations and uses of those words.
    3. The definite and ultimate test here is a random-controlled experiment: try on two groups of people, a control group (using the naive approach) and the optimized one. Which one perform better? However, it is unlikely I would be able to perform such an experiment. Maybe my analysis will encourage someone to do so :)

# How does the optimization works?

It is a simple mix of random + greedy optimization. To select the next article to read:

1. Sample 100 articles from the whole dataset.
2. Select the one of them article that maximizes the learning objective.

# Results of different approaches to learning

One can imagine that the good thing to do is to practice everyday (which is in general a good thing to do). Normally, you will focus on a couple of topics that interests you, read an article from here or there. Basically, this mounts to picking up random articles (to some extent).

This is how your performance will look like this:

[![](https://osm3000.files.wordpress.com/2022/06/something_2-2.png?w=1024)](https://osm3000.files.wordpress.com/2022/06/something_2-2.png)

Progress in achieving the objective if you pick up articles at random (in blue) vs using an optimized/curated set of articles (in orange)

Here you see the traditional wisdom of diminishing returns (or in some avenue that 80-20 rule), which is expected. You progress fast at the

It is very difficult to hit the objective in this scenario of 100%.

However, with optimized articles, we can see that it you can hit your objective in less than 400 articles. The difference is massive!

# _Years_ distributions for both strategies

- ![](https://osm3000.files.wordpress.com/2022/08/random_years_distribution.png?w=1024)
    
- ![](https://osm3000.files.wordpress.com/2022/08/optimized_years_distribution.png?w=1024)
    
- ![](https://osm3000.files.wordpress.com/2022/08/years_absolute_difference-1.png?w=1024)
    
    This is the frequency of years for optimized strategy - random strategy
    

Is this difference statistically significant? YES! And visually clear too! For years 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022. This is basically all the visually different years that you see in the previous graphs.

There is also a difference between both strategies in focusing on different years. We see the years from 2014 until now having increasing importance for the optimized strategy, in comparison with the random strategy.

# _Topics_ distributions for both strategies

I have also looked the category of topics from which these articles come from. This one wasn't clear how to analyze to how look at.

I will spare you the line the thinking and all the annoyances that came with it. But let's say the final outcome is this specific question: given the two strategies, is there a difference between the frequency of the topics in both cases?

If we consider the frequency only and consider the top 25 topics only (from each strategy, there is around 295 topics generated), we can see that there is a statistical difference almost in every topic. Which is COOL! until you see what that looks like exactly.

[![](https://osm3000.files.wordpress.com/2022/06/top_25_topics_means-1.png?w=1024)](https://osm3000.files.wordpress.com/2022/06/top_25_topics_means-1.png)

The percentage of appearance (on the X axis) for difference topics in both strategies. Although you can see some differences, it is hard for me to say that these are fundamentally different.

It is hard to make such conclusion of significance difference visually, unlike in the case of the years. The differences increase when the topics are less frequent, but that is not a surprise. From one side, maybe a bigger sample is needed to get a good estimation about the actual distribution of the topics in the data, and from the other side, the optimization might have been working too hard to squeeze any drop of performance from anywhere.

So, instead of frequencies, I looked at the ranking of 25 most important topics in both strategies. Now we can start to more clearer differences.

[![](https://osm3000.files.wordpress.com/2022/06/top_25_topics_ranking-2.png?w=1024)](https://osm3000.files.wordpress.com/2022/06/top_25_topics_ranking-2.png)

Looking at the ranking of the topic instead of the frequency gives a different perspective. High ranking means high frequency. Some differences exist for the top topics. But when you go to the lower topics, the differences become much clearer.

For the first 14 topics, the differences are not that much, but for the next 11 topics, we can see clear differences. For example, there is almost 10 points difference in the ranking 'sciences' between both strategies.

# Closing remarks

I hope I have given an indication to support the case for optimized strategy _vs_ a naive one.

On the surprising part for me: I didn't expect that some years are more important than other years! I didn't it for the Lolz mainly, but that was a cool outcome.

I am not surprised that there is a difference in the topics, but the dimensions of this difference (like in the topic 'sciences' for example) are surprising for me.

# Things to consider for later

What I like about a project is when it breeds new projects and ideas, and new questions to address :)

1. Some parts of this analysis were very time consuming from the computer, and multiple activities were using a fraction of the computer power, but they were blocking activities. This is really annoying. Fast iterations are key in order to explore new ideas. There are few directions I am considering from this point:
    1. I need to profile each piece of code that I wrote: in general, this is a good practice. There can be ways to increase the efficiency from one, or a need to rethink about the problem in a different way that is more efficient. As a good rule of thumb, there is usually a better way.
    2. Use statistical samples instead of doing exhaustive search: I think this is the direction I am more interested in, and closer to my experience. The main challenge for me in this project is to move from the 'exhaustive' mindset to a statistical mindset. I definitely underestimated the time needs in this project.
    3. Use different framework: I intend to explore Spark for NLP at one point. I don't yet what it can bring to this type of analysis. To be seen.
    4. Invest more in pre-processing: for example, extract a bag of words for each article in advance, and store it in the database. That will make it easy to perform some aspects of this analysis. However, this does have its drawbacks.
        1. In this kind of exploratory projects, it is hard to know what do I want in advance. The questions evolve with time.
        2. The hard disk consumption is high (~30 Gb already for the current data). Adding a lot of metadata just because I can will add extra storage usage, which is not wise at the moment.
    5. Moving the work to a bigger machine: happening soon.
    6. More emphasis on using the database: yes, I still have the tendency to use '.json' files over proper use of the database. In the case of NLP tasks like this, I am not sure what a scalable workflow looks like.
2. I am considering building a small web app, in order to test this. I want to try this on myself first, and make it available for other who would like to try as well. Would I actually improve my French? Will I, at the very least, master 80% of the words? (I know how to form the sentences, the vocabulary for me is a critical point).
3. Why some years are more vocabulary-rich than others? For the years, after discussing with a couple of friends, it might be due to certain unique events that happened at those years. For example, 2001-2002 was the terrorism events, with new words suddenly becoming more dominant. A similar story can be said about 2020-2021, with the lovely era of covid. I will think about a way to analyze this.
4. In my analysis, I considered both the years and the topics separately. It will be interesting to consider both of them together.
5. Adding more 'natural' sources of data: like twitter/reddit/movies & TV-series subtitles. After all, the language LeMonde doesn't necessarily represent what the language of the normal French person.  
    

If you have some suggestion, comment or a feedback, I would love to know and discuss it :)
