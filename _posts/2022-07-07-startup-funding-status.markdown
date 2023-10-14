---
layout: post
title:  "Startup funding status (France and UK)"
date:   2022-07-07 00:00:00 +0200
categories: startups funding
---
I was curious recently about what is happening in the startup world, given the grim expectations for the economy.

**The question is simple: how the startup funding is affected by the recent expectations in the economy?**

To answer this question, I used the data from Crunchbase to get the information about the following types of funding: pre-seed, seed, series-a, series-b and grants, for both France and UK. I got the data for the period from 01/01/2020 to 30/06/2022 (to give a context).

The word on the street is that pre-seed and seed are fine (they are long term investments, and investors need to keep their money working), and that funding will tighten up for later investment stages.

One analysis I was referred to [this analysis for the US startup world](https://jordanpascasio.substack.com/p/2022-q1?s=r). In a nutshell, what it concludes is that seed rounds will not be affected (it might increase), but later stages of funding will be affected. The idea is that other markets (in Europe) will follow the same. Unfortunately, getting the data for the US is more difficult (I am only a starter package from Crunchbase), thus I could verify the claims in the article.

# Highlights:

1. The number of funding rounds for Pre-Seed is steadily declining for the last 3 quarters.
2. The amount of money raised in Pre-Seed and seed didn't decrease accordingly, suggesting it is becoming more concentrated (more money per round).
3. The number of seed rounds is declining sharply in the last 1-2 quarters, same for the amount of money for this stage.
4. While there is a change in the numbers for Series-A and Series-B in the last quarter, there are no clear patterns yet.

# \# View 1: Number of funding rounds

One thing the original article doesn't mention is the number of rounds. They discuss it only from the perspective of total capital invested. So it is hard to know if more capital is allocated to fewer startups.

Looking at the number of funding rounds, you can see interesting trends. I will look at it per quarter (after too many views, this one is much less noisy and more clearer than the others).

- ![](https://osm3000.files.wordpress.com/2022/07/uk-performance-quarter.png?w=1024)
    
- ![](https://osm3000.files.wordpress.com/2022/07/france-performance-quarter.png?w=1024)
    
    Looking at the number of rounds for each type of investment per quarter.
    

Pre-Seed: we can see that both UK and France are experiencing decline in the number of rounds of the last 3 quarter already, beyond the lowest levels since Q1-2020.

Seed:

- UK: it is already declining in the last 2 quarters. Last quarter in particular is pretty steep.
- France: It declines very steeply in the last quarter.

Series-A:

- UK: It went down in Q2-2022, but there is no clear pattern yet.
- France: After a huge jump in Q1-2022 (Can someone explain this to me?), it is going down in Q2-2022. There is no clear pattern yet.

Series-B:

- UK: It went down in Q2-2022, but there is no clear pattern yet.
- France: it seems to hold steady for many quarters already, and in Q2-2022, it even increased!

Grants: for both UK and France, the number of grants have declined in last quarter, but compared to previous patterns, nothing is out of the ordinary yet.

_One interesting thing to note is the slope of decline: the earlier the funding stage, the faster the decline (larger slope)._

# \# View 2: Money raised

The original article focused only on the money raised. Thus, I wanted to explore this particular point.

**Warning**: some reported investment rounds on Crunchbase don't declare the amount of money raised. For UK: 4550 declared vs 1242 not declared, and for France, I have 1227 declared vs 261 not declared. In order to address this problem, I statistically filled the gaps (sample a value from a multi-nomial distribution fitted on the same investment stage for the same year and quarter).

- ![](https://osm3000.files.wordpress.com/2022/07/uk-money_raised-quarter-2.png?w=1024)
    
- ![](https://osm3000.files.wordpress.com/2022/07/france-money_raised-quarter-2.png?w=1024)
    

Pre-Seed: it is hard to determine a pattern here.

Seed:

- UK: It is steadily decreasing in the last two quarters.
- France: it decrease a lot in the in the last quarter. Yet, no clear pattern.

Series-A: for both UK and France, I can't see a pattern here.

Series-B:

- UK: last quarter was unprecedentedly low, with a very steep decline.
- France: it went up! Not sure how to explain that.

Grants: no clear pattern to observe both countries.

This is in general strange. I was expecting the pattern for the amount of money raised to follow the number of funding rounds.

# View 3: Amount of money raised VS number of funding rounds

Following view 2, I wanted to see more what is the relationship between both the total amount of money raised, and the number of funding rounds.

This is the correlation table here:

[![](https://osm3000.files.wordpress.com/2022/07/screenshot-2022-07-09-at-13.39.35.png?w=500)](https://osm3000.files.wordpress.com/2022/07/screenshot-2022-07-09-at-13.39.35.png)

Pearson correlation between the total amount of money raised and the number of funding rounds for each funding stage, in UK and France.  
Pearson correlation coefficient is between -1 (inverse linear relationship) to +1 (positive relationship). The closer to zero, the less the relationship is.

While Grants, Seed (to some extent), Series-A and B are expected (the more the money, the more the funding rounds, and vise versa), Pre-Seed is interesting.

1. It is weakly correlated in France. This explains the weird phenomena: The total money raised didn't decrease, while the number of rounds decreased. The money is becoming more concentrated on some directions.
2. It is negatively correlated in UK! The more money existing in the market, the fewer the number of funding rounds. But the less money existing in the market, the more the number of funding rounds it goes to!

# Things to consider

1. I am not 100% sure if the data on Crunchbase is really up to date in France. I checked a couple of pre-seed startups that I know of in France, and I couldn't find relevant information about them. It might be complete enough to capture the general picture though (if you have insights about this, or you know other sources of raw data, please let me know).
2. I need to analyze if there is a time lag between France and UK. Just for fun!

I would deeply appreciate if you can share opinions or different ways of reading this data, or different sources of data.
