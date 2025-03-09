---
layout: post
title: "The kebab and the French train station: another view"
date: 2025-03-09 18:27:27 +0100
tags: [project]
excerpt: Another take on the effect of distance between the train station and the quality of the kebab...
published: true
---
# Introduction

A few days ago, [I read this cool article posted on HackerNews](https://www.jmspae.se/write-ups/kebabs-train-stations/) that investigated the truth behind a French saying: "The closer to the train station, the worse the kebab."

As a Frenchman living in Toulouse, I felt duty-bound to defend my country's kebab sovereignty against this Swedish incursion 🥖🍷🇫🇷

I mean, what's next? Tacos??

<!-- ![](https://www.goodfreephotos.com/cache/vector-images/challnege-accepted-stickman.png) -->

<img src="https://www.goodfreephotos.com/cache/vector-images/challnege-accepted-stickman.png" alt="NEVVERRRR" width="100"/>


In all seriousness though, I loved the mentality, and I was initially curious about how is it in Toulouse. But if I am investing the effort, then why not build investigate other French cities as well?

I also felt, as the author stated, that the analysis fell short (spoiler alert: it didn’t 😃).

Given that I never worked with GIS data before, that seemed like a good excuse to start.

[My code is available here.](https://gist.github.com/osm3000/ca31bfa400af099a82783cd1ec97130a) Knock yourself out.

# Revisiting the data collection steps

## Correcting some issues

To get the list of the stations using `Open Maps`, the author in his code added the tag `railway=train_station_entrance` 

![Screenshot 2025-03-08 at 22.17.49.png](/assets/images/kebab_analysis/Screenshot_2025-03-08_at_22.17.49.png)

However, such a tag does not exist ([see the list of OSM map features](https://wiki.openstreetmap.org/wiki/Map_features)). 

The right move was to use the `railway=station` tag (which will yield both cargo and passenger stations), and then filter on `public_transport==station` (to get the passenger only stations).

![Screenshot 2025-03-08 at 22.21.24.png](/assets/images/kebab_analysis/Screenshot_2025-03-08_at_22.21.24.png)

So in essence, the main objective - the "Gare" - is not there (intentionally at least).

Besides, the original saying state "Gare", the railway station, not subway stations, and not a RER (Regional Express Network) station.

If we limit the analysis to that, I can end up with a manageable problem.

## Let’s get the train stations only then

Well, easy to say. I spent many fruitless hours on this.

1. Get it from OSM: I tried every combination of filters / tags from [map features](https://wiki.openstreetmap.org/wiki/Map_features), but the results, consistently, keep returning subway and regional express stations! Frustrating!
2. Get it from Google Maps Places API: I tried to search for "Gare", "Gare, Paris, France"…only one results (definitely not a Gare) came. Then I tried "train station"…many results came! BUTTTT, some subway stations still existed.
    1. It seems to be confusing the regional train (that connects the extended Paris) with the traditional train (that goes outside Paris). Gare is only given the stations of the later category
    2. Looking back, the results were actually decent, but by that point I had become too frustrated with Google's API documentation to consider using it. No compromises.
        1. Just make sure to have a suitable location bias…things will get wild otherwise.
3. Finally, I checked online. SNCF,, the operator of the French railways, [has a list of all the Gares in France, ready to export](https://ressources.data.sncf.com/explore/dataset/liste-des-Gares/table/?location=6,46.90879,1.85167&basemap=jawg.transports). Although, after careful investigation, I found the "[Gare de Lalande-Église](https://fr.wikipedia.org/wiki/Gare_de_Toulouse-Lalande-%C3%89glise)" in Toulouse listed, which is permanently closed since 2016 (its name now is "Ancienne Gare de Lalande-Église". There is no filter on such closed stations, and I don't know how many of them (and other issues) exist...but I was ready to give up this fight by now.

This makes the problem more tractable. For Paris for example, instead of 1181 stations (in the author’s original post), or 247 after correcting for the OSM applying the proper tags and filters as mentioned earlier (which didn’t work well to my liking still), now it is only ***42***. 

This should improve also the analysis…

## The dense-city problem

Given the large number of stations the author took into account, I believed that this will lead to distorted results. The problem with dense cities is that trains and metro are all very close to each other. The furthest from one station is probably the closest to another station.

So when analyzing "the distance to the nearest station entrance for each establishment", one can run into many unwelcome overlaps.

By committing to the analyzing "Gare" only, the problem of density resolves itself. The stations - even in a packed city like Paris - are sufficiently far away from each other. Sure, you will argue that in Paris, "Gare de l’Est" and "Gare du Nord" are almost across the street from each other. But that is not that bad. Other than this cluster, this case doesn’t repeat itself.

## Adjusted rating

It is problematic to compare ratings to each other, given that the number of reviews are not the same.

So, I am going to correct this. I can create a new adjusted rating that will take the number and distribution of reviews into account…

Life will be amazing, justice to the poor, viva la France, yaaayyyy…..

[Except…the API can return 5 reviews only at max](https://featurable.com/blog/google-places-more-than-5-reviews). That took a couple of hours of debugging…

So, unfortunately, I will have to rely on the final rating only.

## Collecting the restaurant data

After some trial and error, I found the author’s approach of just searching for the word Kebab to be sound. Thus I followed it.

Given the limited number of station points that I am using (tighter definition), this results were 198 restaurants for Paris, which is manageable. 

# GIS assumptions

Since GIS is not my strong item, and I that didn’t think this ultra accuracy / data integrity is necessary (I mean, I am using a Google API that doesn’t provide comprehensive results, with ratings of questionable quality, with no access to the individual ratings, let alone the review), I am going to assume that the relevant distance is euclidean distance (thus ditching the "walkable" distance). Why?

1. Large cities in France tend to be very dense and walkable. Thus, I suspect (without providing any evidence) that the euclidean distance will correlate nicely with the walkable distance.
2. A problem can arise when there is a river inside the city. This can screw up things badly. But, normally if the river / canal is narrow, there are crossing in front of the station (anecdotal evidence, I need to find a better way to tackle this). This is not the case if the river is wide, then we are fine (far away is truly far away).

## Notes on the GIS data

From the original post:

> all data was projected to `EPSG:32631` (`UTM zone 31N`).
> 

What the hell is does any of that mean?

After some googling, apparently the longitude and latitude are not great to calculate distance between geographical points. To correct for that, you need to project to the [*Universal Transverse Mercator (UTM)*](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) coordinate system, which it is a horizontal position representation that ignores altitude and treats the earth surface as a perfect ellipsoid. It divides the world into 60 zones, each represents a plane with its own coordinates based on the [*World Geodetic System (WGS 84)*](https://en.wikipedia.org/wiki/World_Geodetic_System).

You can find out the relevant zone from many website like [this](https://mapscaping.com/latitude-longitude-to-utm-converter/). Both Paris and Toulouse are in `UTM 31N` zone.

These zones have ISO-like codes called `EPSG` , which are better for computers (I guess). Once you have the UTM zone, you can get the `EPSG` [code from here](https://spatialreference.org/ref/?search=WGS+84+%2F+UTM+zone+31N).

In France, Paris and Toulouse are in the north hemisphere `N` in zone `31` , thus `UTM 31N` , which also has the `EPSG` code  of `32631` .

<!-- ![How the hell did he get the Paris Polygon?](https://openclipart.org/download/215664/Computer-Guy.svg)

How the hell did he get the Paris Polygon? -->

<p style="text-align: center;">
    <img src="https://openclipart.org/download/215664/Computer-Guy.svg" width="200" alt>
    <br>
    <em>How the hell did he get the Paris Polygon?</em>
</p>


## Google Maps: Rest API vs Python SDK

What a weird question! Both are the same!

Yet, for the life of me, with the python SDK, repeating the author’s original step never worked for me.

![Screenshot 2025-03-08 at 14.13.53.png](/assets/images/kebab_analysis/Screenshot_2025-03-08_at_14.13.53.png)

Several hours later…no resolution.

Accidentally, I realized that when using `cURL` with the URL directly works pretty well!

So, to move on my with life, [I wrote a wrapper around it instead](https://gist.github.com/osm3000/ca31bfa400af099a82783cd1ec97130a#file-kebab_analysis-py-L56).

# Results

To recap, I want to get the assess the relationship *between the restaurant rating and the inverse of the distance between that restaurant and the train station*.

I decided initially on a distance cut-off of 1000 m (who wants to go that far anyway for a kebab?). While calculating the coefficients, I also trained a random forest classifier (distance and an input, and the ratings thresholded by their median as the output), in order to keep an eye on non-linear relationships. 

The main non-linear source I had in mind is thresholding effect: that the relationship between the distance and the rating changes after a certain distance cut-off. Thus, the more positive the coefficient, the stronger the support for the initial claim.

With the distance cut-off of 1000 m, the coefficients in general seemed low (with a couple of exceptions), while the F1 score of the classifier was high enough (you can check the logs here). This triggered me to try 500 meters, which indeed resulted in different picture (albeit at the cost of reducing data points).

| City        | Nb of data points at 1000 m | Coeff at 1000 m | p-value at 1000 | Nb of data points at 500 m | Coeff at 500 m | p-value at 500 |
| ----------- | --------------------------- | --------------- | --------------- | -------------------------- | -------------- | -------------- |
| Paris       | 350                         | -0.018          | 0.7406          | 109                        | 0.119          | 0.4761         |
| Toulouse    | 37                          | -0.087          | 0.6089          | 6                          | -0.474         | 0.5371         |
| Lyon        | 38                          | -0.128          | 0.4436          | 14                         | -0.104         | 0.2054         |
| Marseille   | 30                          | -0.056          | 0.7676          | 23                         | 0.031          | 0.6218         |
| Lille       | 20                          | -0.102          | 0.6677          | 1                          | -              | -              |
| Bordeaux    | 2                           | 1.0             | 1.0             | 0                          | -              | -              |
| Nantes      | 4                           | 0.221           | 0.7793          | 3                          | 0.314          | 0.6674         |
| Strasbourg  | 11                          | **0.606**           | **0.048**       | 4                          | 0.744          | 0.5865         |
| Rennes      | 18                          | 0.023           | 0.928           | 2                          | 1.0            | 1.0            |
| Montpellier | 20                          | 0.08            | 0.7384          | 11                         | 0.352          | 0.3628         |

Now, looking at these results, while the coefficient results are interesting in case of 500 m, there is clearly weak statistics all over place, except for Strasbourg!

Only Strasbourg at 1000 m (and 750 m, not reported here) except a strong pattern that indeed, the closer to the train station, the worse the kebab.

Thus, the logical conclusions from this utter waste of time are:

1. France, in general, doesn’t have a kebab issue near the train station. More scientifically, these is not enough evidence to refuse that "there is no linear relationship" hypothesis...but it just it doesn't look promising.
2. Strasbourg is German

So, indeed there is no sufficient evidence for a linear relationship between the distance to the station and the quality of the kebab…

Technically speaking, we addressed the raised issue, given the available data…

But what about non-linear relationship? 

## Exploring the non-linearity

(this is mental-prostitution section, feel free to skip it if you have anything to live for)

<!-- ![](https://c8.alamy.com/comp/HT5CK3/cartoon-vector-doodle-stickman-sitting-in-front-of-the-computer-and-HT5CK3.jpg) -->

<p style="text-align: center;">
    <img src="https://c8.alamy.com/comp/HT5CK3/cartoon-vector-doodle-stickman-sitting-in-front-of-the-computer-and-HT5CK3.jpg" width="200" alt>
    <br>
    <em></em>
</p>

P-value is extremely limited concept, in the sense that it assumes a linear relationship. 

I am a big believe in predictive power analysis. Basically, build a good machine learning predictor model, and infer some aspects about the data from the model performance / characteristics.

Now, to do this properly, one should try different models and hyper-parameters, but this is an overkill for this problem, so I will just use `Random Forests` with default settings from `scikit-learn` .

I am also not a big fan of studying regression models (continuous is overrated), so I will make a modification here. I will create threshold the ratings based on the median of the restaurants ratings in that city. Thus, the new score is 1 (good kebab) if the ratings is above the median, 0  (bad kebab) otherwise. This gives me a nice balanced dataset.

To get some statistical sense, I report the results on a 5-fold cross validation.

Interestingly, in the majority of cases, the model performs better (or far better) than random!

To be extra careful (since the balance can be 45-55% sometimes), I am going to report the F1-score (the things that we chose to care about….).

But since we are at it, why only focusing on the distance? we can study the angle from the station as well. Why? My hunch was that one side of the station is not the same as the other side

For the sake of brevity, I will report the average F1 scores on the 1000 meter cut-off only here

| City        | F1 score: distant only | F1 score: distant + angle |
| ----------- | ---------------------- | ------------------------- |
| Paris       | 0.735                  | 0.773                     |
| Toulouse    | 0.438                  | 0.453                     |
| Lyon        | 0.667                  | 0.48                      |
| Marseille   | 0.579                  | 0.603                     |
| Lille       | 0.393                  | 0.213                     |
| Bordeaux    | -                      | -                         |
| Nantes      | -                      | -                         |
| Strasbourg  | 0.693                  | 0.867                     |
| Rennes      | 0.133                  | 0.593                     |
| Montpellier | 0.333                  | 0.493                     |

Except in Lille and Lyon, clearly having the direction of the restaurant provides a significant value.

We can no claim there is a pattern in Paris - Marseille - Strasbourg - Rennes between the rating of the kebab restaurant and its distance / distance & angle from station.

But what does this look like? Let’s use our X-ray googles, and look at the decision boundaries of the model. Let’s start with Paris, with both distance and angle being used.

![Paris_decision_boundary_angle:True_1000m.png](/assets/images/kebab_analysis/Paris_decision_boundary_angleTrue_1000m.png)

For understanding, the station exists at distance 0 and angle 0. Color yellow indicate a good Kebab, and 0 for dark…whatever it is…indicate a bad kebab.

Now this is cool! Basically there are areas / clusters for good kebab, and clusters for bad ones. It is like looking at rooms of a large flat, with each room being occupied with people of similar interests.

Looking at Strasbourg, that clearly explain a lot of things!

![Strasbourg_decision_boundary_angle:True_1000m.png](/assets/images/kebab_analysis/Strasbourg_decision_boundary_angleTrue_1000m.png)

So there is a couple of good kebabs very close (almost inside) the train station, then bad kebabs after that, the good kebab after the bad ones (this just reminded me of poor Kif in Futurama: the beautiful women, then the large women, then the petite women… 😃).

[https://youtu.be/AwOJ2S6iM6g?t=36](https://youtu.be/AwOJ2S6iM6g?t=36)

So probably the saying should be: the quality of kebab depends non-linearly on both the distance and angle of the restaurant from the train station….

I am sure this is going to be catchy one day in the common culture.

# Finally

First of all, that was fun. Many thank for the original author (James Pae) for starting this :)

Second, while surely this is just Kebab, it is really disturbing to me that we can’t have access to existing higher quality data (like the Google reviews, or the individual ratings). In parallel with the "right to repair" move, we need the "right to know" move. These leftover datasets are of limited use. While not everyone is expected to dig in the data, some will, to help ourselves make a better and informed decisions.

# Code
<script src="https://gist.github.com/osm3000/ca31bfa400af099a82783cd1ec97130a.js"></script>