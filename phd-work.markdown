---
layout: page
title: My PhD Work
permalink: /phd-work/
published: true
comments: This needs to be heavily revised. The whole concept of the task and style doesn't make much sense to be. There is a need for "lowest common denominator" component.
---

My PhD focus was on studying a problem called _styles_ or _personas_, using deep neural networks. You can find the whole manuscript [here](https://www.google.com/url?q=https%3A%2F%2Ftel.archives-ouvertes.fr%2Ftel-02488856%2F&sa=D&sntz=1&usg=AOvVaw3ceDR4XaqtfO4mOVohrkgq). The papers published during this period can be found [here](https://scholar.google.com/citations?user=FpRt65QAAAAJ&hl=en).

## But what is a style anyway?

Long story short, whenever you do something, there are two components: what you want to do (task), and how you do it (style).

An example when you say the word "_seriously?_". Depending on the manner you say it, it will carry different meaning (sarcastic or surprise for example). One task, two different styles, two different results in this case.

Another example is writing. You can the same the letter (the task), but with multiple fonts (the style). In this case, you are perceiving the final shape of the letter (the letter image).

<!-- ![](https://osm3000.files.wordpress.com/2022/06/different-fonts.jpg?w=960)

![](https://osm3000.files.wordpress.com/2022/06/difference-in-style-perception-1.jpg?w=960)

![](https://osm3000.files.wordpress.com/2022/06/difference-in-style-perception-2.jpg?w=960) -->

<figure><img src="https://osm3000.files.wordpress.com/2022/06/different-fonts.jpg?w=960" alt="Trulli" style="width:100%"><figcaption align = "center"><b>Different writing styles that is clear at the end</b></figcaption></figure>
<figure><img src="https://osm3000.files.wordpress.com/2022/06/difference-in-style-perception-1.jpg?w=960" alt="Trulli" style="width:100%"><figcaption align = "center"><b>Two letters that look exactly the same, but....</b></figcaption></figure>
<figure><img src="https://osm3000.files.wordpress.com/2022/06/difference-in-style-perception-2.jpg?w=960" alt="Trulli" style="width:100%"><figcaption align = "center"><b>when you look at the dynamics, you can see they are actually different: the green dot is the starting point of the drawing. The solid red arrows represent the pen strokes and their directions. The dotted arrows represent the air strokes (the movement of the pen without touching the paper)</b></figcaption></figure>

But it is different when you look at the writing dynamics.

What is the difference between the two drawing of letter **X** on the left? hmm, nothing.....right?

But what if we look at the pen movement for each letter, something interesting is noticed:

- The writer for the left letter starts from top left, and proceeds to draw the letter counter clockwise.
- The writer for the right letter starts from top right, and proceeds to draw the letter clockwise.

This is not apparent at all when you look at the final product (i.e., the image of the letter), but once you look the pen sequence, you can see the difference.

Question here: would you consider this as a style or not?

The answer is: it depends on what you care about! And this is a big difficulty.

The concept of style is ill-defined (it is not always clear what is the task and what is the style), and it differs from one field to another. It also depends on which angle of you are looking from. Let's go back to the writing example: In the previous examples, we know the task. We can describe it clearly. But is this always the case? In simple cases, probably yeah, but if you have a complex sequence of behavior (lets say two people interacting with each other), the set of tasks are diluted and unclear.

In such realistic scenario, there has to be a heuristic first to divide the sequence into a set of tasks, and then explore the styles of one of those tasks (or at least some of them). We can consider those as _local styles_.

There could be also some _global styles_ (high tone of voice for example, defensive or offensive attitude,....etc).

_**I did not handle these cases during the PhD though. I always worked within a well-defined task definition.**_

## Why studying styles? what is the final objective?

[![](https://osm3000.files.wordpress.com/2022/06/nina_robot.jpg?w=570)](https://osm3000.files.wordpress.com/2022/06/nina_robot.jpg)

iCub robot, Nina (GIPSA Lab)

Our long-term objective is to enable our humanoid iCub robot [Nina](http://www.google.com/url?q=http%3A%2F%2Fwww.gipsa-lab.grenoble-inp.fr%2Fprojet%2FNINA%2Fhome.html&sa=D&sntz=1&usg=AOvVaw2AbeaZXRmBb_5LP-zpUBHj) to exhibit personalized behavior suitable for the person interacting with it. This will enhance the user experience, and will allow for a more natural interaction with the robot.

At the moment, we successfully used machine learning approaches in order to build models of human-robot interaction. However, when using these models to generate behaviors, this behavior usually represents an average over the learned behaviors (which is expected).

The goal is to learn models of styles, and use it to bias the models of interaction that we have, in order to generate more personalized behaviors.

## What am I doing exactly in the PhD?

My PhD focus on studying styles, given that the task is well-known, using deep learning approach. In particular, we were concerned with the following questions:

1. Propose a framework to study styles
2. What kind of benchmarks are suitable for comparison?
3. How to extract styles?
4. If we learn some styles, can we leverage them to accelerate the learning of new styles? (i.e., transfer learning of styles?)

After many over-complicated or over-simplified approaches, we settled on the use of _Deep Autoencoders_ as the basis to study styles.

### Propose a framework to study styles

If you know the styles in advance, and you have labelled data for these styles (i.e., you have explicit knowledge of the styles), congrats, you are with the classification framework! You can have explicit evaluation of the styles as well (via metrics like accuracy and F1-score for example).

- I assumed styles to be categorical here (ex: say clockwise vs counter clockwise in drawing letter X), but they could be continuous as well.

But what if you don't know (as it is usually the case), then how do you study styles? Explicit study and evaluation are out of the question in this case.

### The assumptions in our work

- A notion of a task is known beforehand.

## A word about tasks and style (perspective)

Identifying the set of relevant tasks and styles is contextual; it depends on the context you are looking at the problem.

The way I think about it is that: the problem is fixed, but can't be observed. Depending on the context, we can see an aspect of the problem (styles + task).

One can imagine this as having a light bulb directed to a some geometrical body. We can only observe the shadow. The shadow tells us a bit about the body, but not the complete fact. Depending on the direction of the light bulb, the shadow will change, showing us a different aspect for the problem. Stretch your imagination a bit and imagine the shadow has colors as well, depending on the direction of the light bulb, its distance, and some aspects of the problem. On can imagine in this case that a task in this case will be the geometrical shape of the shadow (a container), and the style is the coloring of the shadow.

Lets take handwriting as an example: the problem is handwriting. Letter "_**E**_" is an example of handwriting (a shadow resulting from the light bulb being at some angle). The shadow colors that f it in the resulting geometric shape are the styles of letter E (**also, mention that the bulb not only determine the letter, but also the context -- are we looking at a picture or the movement sequence of the pen).**

### Food for thought

- Instead of trying to model the problem itself (which we don't have access it), can we model the light bulb possible movement instead? Then, can we compile all the resulting shadows from lots of light movement, in order to get to see the actual problem?
- Problems can have problems inside them, depending on the level of granularity (another context) that you look at the problem: consider drawing as a problem. Handwriting can be an aspect of drawing, and maybe we can study handwriting as a whole. We can also look at handwriting as the problem, and the individual letters as aspects of handwriting. We can look at letter **A** as a problem, the sequence of micro-movement that construct letter A as the aspects, and so on.
    - Matter can be divide into pieces, and the pieces into smaller pieces, ...etc, tell we reach the atoms, then we can divide the atoms into internal components, and so on
- The genius really is to define the the limits of what you are looking for, and develop solutions that fit that limit.
