---
layout: post
title:  "Parallel is not always good"
date:   2023-11-11 00:00:00 +0200
categories: experiments
tags: [programming, bug, evolutionary algorithms]
---

Without fully understanding what is happening under the hood, parallelizing your code can lead to slower performance.

# Context
I am working at the moment on evolutionary optimization for neural networks, to train agents to play games. To give a fitness for the neural network, the agent need to play N games (starting from random position), and the fitness is the average score of those N games. These N games are being played in parallel (using `multiprocessing` library in python). 

In this case, I've 32 cores available, and I am running 32 games in parallel.

The stack here was simple: `python` for the code, `python-arcade` for the game design, `pytorch` for the neural network, and `pygmo` for the evolutionary optimization.

# The problem
The problem is that the speed of execution. It was abysmal. I was getting individual (aka: 32 games played) in ~5 seconds. This is a very long time for a super simple game. I was expecting something in the order of milliseconds.

In general, especially early on in the experimentation process, a long optimization time is always a sign of bad design, and that I am doing something wrong.

# The investigation
My first thought was that it is `python-arcade` that is the problem. I went deep into the package, and had conversations with some of the developers on the discord channel. My suspicion was geared towards the game clock. Each game needs a ticking clock. The clock speed determines the number of frames per second. My hunch was that in a headless mode though, the same clock is being used, thus the bad performance (basically, in `headless` mode, I want the clock to tick AS FAST AS POSSIBLE).

I was wrong: there was no clock in the headless mode. The problem was somewhere else.

My next thinking was: it has to be that `python-arcade` itself is slow. This was a half-ass guess, but in this elimination process, I need to rule it out. So, I built a game engine from scratch (that operates on a matrix of ascii characters). Things can't get any faster than this.

Run the optimization, and lo and behold....there is almost no gain whatsoever! 

Almost ready to surrender, I then converted the multiprocessing evaluation into sequential evaluation, just to set a benchmark and record my observations for later. To my sheer surprise, the was a phenomenal gain in speed!

I need to dig a bit deeper into this (profile the code properly), but I am nearly confident now it is because of how `pytorch` works: the library is already very efficient in using the different cores. Having many instances of a `pytorch` library is most likely to choke the available CPU resources, leading to this excessive delays.

I probably need to invest more on my debugging / profiling skills: elimination process is cool and effective, yet bloody expensive.

....hard lesson learned.