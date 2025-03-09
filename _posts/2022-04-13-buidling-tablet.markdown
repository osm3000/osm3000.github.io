---
layout: post
title:  "Building my own tablet"
date:   2022-04-13 00:00:00 +0200
tags: [projects]
categories: electronics engineering thinking
---

Over the last couple of years, I came to the conclusion that I need to have a higher degree of control over my environment:

- I need to be able to optimize the items in a way that is suitable for my own usage
- I want to be able to repair my stuff when they break, or upgrade the necessary components only (I am deeply affected by the _right to repair_ movement).
    - I would highly recommend watching this [mini-series](https://www.youtube.com/playlist?list=PLTlJK3kwZIbSKCvNBA53Mdx4nST5TZs4Q) for real-life examples and implications .
- When there is a problem/new need, I want to make a solution to address it, in the way that best fits me

This applies to the software that I am using and to physical items in the room/office.

I've been thinking a lot about privacy and security (for the electronic tools). Even though we know about that these devices (phones in particular) collects huge amount of data through their sensors about me, it seems I am powerless to do anything about it. So, at the moment, I am in the mindset of: let's stop it at the source.

One of these project is to make my own tablet/lightweight laptop. A big motivation is that I need an e-reader. My book situation at the moment is super critical. I wasn't really satisfied was any e-reader I found in the market.

I came to realize during this project that the inability of making my things/the direct acceptance of what is already out there, have destroyed a lot my taste and even the awareness of what I really like and what I don't like. Designing and building things, that I will have to use, led to the emergence of these questions, and to many iterations to understand what I like and I don't like. It is not just an engineering/technical processes, it is a journey inside who I am. It's a process.

I am also realizing that pure consumerism life has negative psychological impact on me. It's like my soul is getting fat. I've to pray that what I need exists on Amazon, and even with that, I no longer knew what I need. I go to get something, ends up with something else irrelevant to the original problem, and the cycle continues.

It feels that, even though somehow the options has increased over the year (you have so many phones from many manufactures available), the actual meaningful choices decreased. It seems that the choices based on the price range increase, but not based on the design choices (all the phones look exactly the same for example! but you will find a phone suitable for each budget).

# Specifications

At the beginning, what I wanted is:

- A tablet for reading: 10-inch touch screen of course!
- Mobile enough: maybe not the same as a commercial tablet, but must be easy to move and get it up and running in no time.
- Long battery life
- 60 GB of storage, 4-8 Gb of RAM.
- Fixable and upgradable: if something breaks, I should be able to fix it/replace the broken parts. I identify the points of fix/upgrade/replace to be:
    - The computing unit
    - The memory (SDcard): replace if there is a problem, or get a larger one.
    - The screen
    - The battery: get a larger/smaller/different battery.
    - The enclosure/support/mounts

# Hardware used

- Computing: I hesitated between a _[Raspberry Pi 4 B+](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)_ (powerful, large, many peripherals, but more power hungry) or _Raspberry Pi Zero_ (less powerful, more compact, less peripherals, power efficient). I decided to go for the _Pi 4_, since it gave me a big room to maneuver in this project. Maybe in a later iteration I will choose something different.
- Screen: in the absence of better judgement, I just choose a screen from Amazon, that has mounts in the back (quite important in order to attach everything to the screen). I choose _[HMTECH Tactile 10,1" 1024 x 600](https://www.amazon.fr/gp/product/B098762GVK/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&th=1)._
- Battery: It was not clear for me what will be my power requirements in general. So I decided to use an external battery laying around, 20000 mAh capacity, for now. There is some estimations for the power consumption of the Raspberry Pi, but I had no clue how much power the screen will consume.
- Cables: I didn't even consider this, but it will play a important role later.
- Creality Ender 3 v2 3D printer: to print any required parts.

# Software

- Operating system: my main requirement is to use a Linux distribution, preferably Debian (since I am familiar with its packaging system). I choose Raspberry Pi OS 32-bit
    - Yes, I can hear you asking: why the fuck did I do that? honestly, I don't know :D I had hopes.
    - The main reason for using Linux is I know how to build my own programs on it when I need so.
- FreeCAD for the design of any required parts.

# Steps

My philosophy in general is not to focus too much on getting things right from the first time (a plague in current engineering unfortunately), but to get a whole pipeline, end-to-end, working ASAP, and then iterate over this pipeline (improvements, adding/removing modules, …etc). I've been heavily criticized for that approach over the years, but time and time again, it always worked perfectly. Iterations of design, deploy and feedback were always perfect. It is my main way to understand the problem in a deep manner (I need to get my hands dirty). Most of the time, the problem statement/definition is vague at best, or doesn't even exist. This definitely applies to this project.

## Round 0: happy with the new toys

[![](https://osm3000.files.wordpress.com/2022/03/img_20220302_134703403-1.jpg?w=1024)](https://osm3000.files.wordpress.com/2022/03/img_20220302_134703403-1.jpg)

Day 1: get all the parts. The PI Zero W (with the red base) was still part of the planning

Getting everything up and running was quite straightforward. Connect the screen to the PI, the PI to the power source, and Voila!

[![](https://osm3000.files.wordpress.com/2022/03/274078076_1320842185084755_597342884531825599_n1-1.jpg?w=1024)](https://osm3000.files.wordpress.com/2022/03/274078076_1320842185084755_597342884531825599_n1-1.jpg)

The whole thing is easy to setup in no time

At the beginning, I did connect the USB port of the screen directly to the power. The screen worked, but the touch capability was not there. After some time worrying, I realized that the USB should be connected to the PI directly. It will draw the power from the PI, and send the touch commands to the PI.

With that, many issues became apparent:

1. The obvious question at that moment was: how to make this whole thing compact?
    1. Where/How to attach the battery and the Rasbperry Pi to the screen?
        1. For the PI, luckily, the screen had a mount for it on the back
    2. What to do with the huge space that the cables are consuming?
2. The screen brightness: It was glowing like the hot sun in the middle of the summer.
3. While the touch worked, it was clear that it doesn't
4. Rotating the screen: in the spirit of using it as an e-reader, I would love to have the screen in portrait orientation instead of a landscape. While this is easy in
5. All the components are exposed: Even after mounting everything, how can I protect them?
    1. The driver
    2. The PI
    3. The ribbon cables connecting the screen to the PI

## Round 1: I hate my life

While thinking about how to resolve all of these issues, I decided that I need to use it more often, in order to get use it.

One day early morning, I took the whole thing, set it up on the table, and started reading. I genuinely hated it. My eyes hurt from the screen. The whole thing is cumbersome.

Since I was still in the touch-based usage mentality, I downloaded a virtual keyboard on the OS. Well, that was hilarious!

<!-- ![](images/img_20220326_173155374_hdr-1.jpg) -->
![](https://osm3000.files.wordpress.com/2022/03/onscreen-keyboard-raspberry-pi.webp)
What the virtual keyboard is supposed to look like.  


![](https://osm3000.files.wordpress.com/2022/03/img_20220326_173155374_hdr-1.jpg)
The keyboard I have...No numbers, no arrows, any control button :(

Also, the icons is quite small, and the heat box is not exactly under my finger. It is not straightforward to click 'X' to close a window.

- This gave me a huge appreciation for what Apple and Samsung did in their phones. There is a good reason why you would need a tight end-to-end control over the software and the hardware, in order to produce a good product. For example, with a proper icons sizing and arrangement of functionality in the OS/software, non of this would have been important.

Many hours later, trying to find a way to configure/change this, but to no avail... I considered this to be a dead-end.

I relied on PC keyboard and mouse from that moment on order to control the device. That was cumbersome: the keyboard is almost double the size of the tablet, and the tons of wires.

Since the whole setup was massive (tons of long/rigid cables), I had to connect/disconnect everything for each time I use the tablet (in order to be able to store it).

I designed a single-piece enclosure for the tablet. I spent so many hours on it (because I was very rusty in drawing in 3-D and the software): places for the PI, Driver, and a whole level for the battery and any other component. Time to print an example (it is important to print a demo, to make sure the dimensions are correct, before committing to the final thing)...just to discover it is larger than the printer! After some adjustment in the positioning of the piece, the demo will take...a day and half to print. Clearly this is not going to work...

After I overcome my hate to myself, I listed the following issues to address:

1. For the enclosure: it is time to print it on several pieces, and fasten them together if necessary. These pieces are: the cover for the PI, the driver and the mount for the battery.
2. Keyboard and mouse: After some thinking, I realize I actually don't like the touch screens in general, especially when I need to write on them. So, I decided to get a mini-keyboard with a touch-pad. I ordered two to evaluate which will work for me.
3. The cables: after some discussions with my flatmates, I got introduced to the world of 90/180 degrees cables. After a long digging on amazon, I settled on new set of cables ([USB](https://www.amazon.fr/gp/product/B07BC5XT4P/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1), [HDMI](https://www.amazon.fr/gp/product/B07VLDS77G/ref=ppx_yo_dt_b_asin_title_o07_s01?ie=UTF8&psc=1)), and shorter lengths (just to fit the design).

## Round 2: Massive improvements

- With the new cables installed, the whole thing became much much more compact. There was no reason anymore to dismantle anything after use.
- The [Bluetooth keyboard](https://www.amazon.fr/gp/product/B01N76LDZH/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) really made a massive change. It doesn't use a dongle. The feeling is good. A bit unfamiliar layout, but I got used to it quickly.
- I didn't realize before I can connect two Bluetooth devices in the same time. When I connected my headphones as well, that was another improvement.
    - Since I am using the Raspberry Pi 4, there is an audio jack. But by now, I've developed an allergy from seeing cables.
- The enclosure: I focused on the protecting the PI at the moment. After many failures (bad measurements, new adherence problems between the filament and the bed of the 3D printer), I finally managed to get it done.
- Software setup: I invested time to add the software I wanted (like VScode), setting up my preferences, SSH keys,...etc. It now became much more usable. Changing the style, colors, all of that, helped a lot to feel "this is mine and I can use it"

![](https://osm3000.files.wordpress.com/2022/03/275720407_653054409103252_6805556995924280321_n-1.jpg?w=1024)

Much less cables than before. HDMI remains a challenge (rigid cable, hard to find the right length), but for now it is okay. The PI enclosure works!

![](https://osm3000.files.wordpress.com/2022/03/275699160_508116540709541_8413618761133755527_n-1.jpg?w=533)

Not so thick finally

![](https://osm3000.files.wordpress.com/2022/03/275230078_1098426160979958_8478573957180597664_n-1.jpg?w=1024)

First time I try the new keyboard and the headphones...it was a couple of hours of pure happiness and satisfaction :))

When I connected it everything together, I listened to some music. It was one of the happiest in my life :) It is hard to explain. I was just...satisfied :)

## Round 3: Finishing the parts

With the previous phase done, I moved on to make the cover for the screen driver circuit. While it is a similar process to the PI's cover, there was an essential question about where/how the battery would fit. There are only two ways to attach the battery in the back: either by a glue, or some holder that will make use of the only fasteners available (the PI's and the screen driver). I am not in favor of gluing expensive components, so fasteners it is. But that means that the screen driver design has to take this into account.

After so many brainstorming sessions and discussions with my flatmates, I finally decided...to not attach the battery. It was heavy (thus, a lot to think about in the design of its holder) and I wasn't yet so sure yet where this whole project is going. Plus, it didn't see to be a big deal to have the battery separated. It allowed for plugging in to the electric socket quite easily when at home, when battery is not needed (thus, saving the battery's life).

I also made two supports/holders for the tablets. These made a huge improvement in the whole experience.

[![](https://osm3000.files.wordpress.com/2022/04/img_20220322_182431902.jpg?w=1024)](https://osm3000.files.wordpress.com/2022/04/img_20220322_182431902.jpg)

Much better organized setup now!

[![](https://osm3000.files.wordpress.com/2022/04/img_20220322_170943540-1.jpg?w=1024)](https://osm3000.files.wordpress.com/2022/04/img_20220322_170943540-1.jpg)

The new supports...neat :)

[![](https://osm3000.files.wordpress.com/2022/04/img_20220322_170957172.jpg?w=1024)](https://osm3000.files.wordpress.com/2022/04/img_20220322_170957172.jpg)

## Round 4: Getting out of the house...will it break?

That was an important challenge, and I hesitated on starting it a lot. But finally, I did. The only thing that had to be dismantled with the screen USB connection to the RaspberryPi (otherwise, there will be too much pressure on this part).

The whole thing WORKED :D I was super happy. Easy to setup, convenient to work with. I went many times for coffee shops. Even did a lot of small codes on it.

I was more happy when I came home, and it still worked fine :)

## Round 5: Multiple days stress testing

You might have read my previous post about analyzing articles from LeMonde. Well, I am preparing for phase two, which includes scrapping ~1.25 MILLION article.

Let's use the tablet to do a part of the job.

For 1 week straight, no breaks, the tablet was assigned the job of scrapping this data from LeMonde. Aside from dust on the screen, everything works perfectly!

# Lessons for the future

1. Getting something functional and running these days is quite easy. Getting something usable is much more difficult.
    1. Details matters. The fact that you can easily carry it, operate it, handle it, really matters. For example, the support/holders that I made, or the bluetooth mini-keyboard, both improved a lot the usability.
2. I didn't realize there are [large ink-screen available (AliExpress)](https://www.aliexpress.com/wholesale?catId=0&initiative_id=AS_20220406122434&SearchText=ink+display)!! Definitely I should have checked there first before I made a decision about the screen.
3. Get a screen that you can control its brightness! Good screen matters a lot.
4. Components in France are just ridiculously expensive (give examples: cables, screen, screws). For such a project, it would have been better to order everything from AliExpress. The main issue was time (the delivery time of AliExpress is quite long, and I was in a hurry). But, lesson for the future.
5. Raspberry PI is a game changer. And I think the whole move towards mini-computers like this is just fucking awesome in general. Having that much capability (computing, memory, peripherals, interfaces, connectivity) out of the box has saved enormous amount of time
6. For the enclosure, I think that for a large flat surface, I am convinced that starting from a sheet of wood/acrylic glass will be the best choice. 3D printing such a surface is problematic (need a large printer, or need to print it in sections and fasten them together). Adding mounts/supports on that sheet for other components can be done with the 3D printers. I am resisting the urge to buy a CNC machine right now :D, but I can definitely see the problems it can solve. Plus, I would love to use acrylic glass (I love to make the electronics and the lights visible). This is an adventure for another time.
7. While the ad-hoc benchmark that I did for the power consumption was very promising (low power consumption, very suitable to use external batteries), I noticed that, during the boot sequence, sometimes the whole thing just shuts-down. My hypotheses were either something is damaged, or there is a power surge near the end of the boot sequence. I removed the monitor (assuming that it is its fault), gave time to the PI to boot, then connected the monitor, but it didn't boot correctly!  
    Finally, I tried multiple power adapters and batteries. It seems to work only with the high-quality ones. So, the lesson here is: a good quality adapter / battery is a must.
8. Go for a 64-bit OS from the beginning :D

# What is next?

1. What to do about the battery? I don't know for sure yet. Should I keep it as it is now, with the battery separated from the device? Should I group some battery cells together, create
2. Make a phone: For me, the phone is my most used computer, and the least controlled one in terms of programmability and upgradability. It will pose a challenge to make it small and compact enough to be usable, but I am curious about this journey to discover what I really want and like, without the previously imposed biases from the current manufactures.
3. Get/build very customized and small cables: To get the size even smaller, and mobility higher, I need to take another look at the cables. Either I will make them from scratch (which I am not very eager to do at the moment), or find some alternatives. Not a deal breaker at the moment though.

# Acknowledgement

Many thanks for [Dom Wallis](https://www.linkedin.com/in/dominic-algernon-wallis-123b42187/), [Juliette Jaupitre](https://www.linkedin.com/in/juliette-jaupitre/), [Firas Mourad](https://www.linkedin.com/in/firasmourad/), for their inputs, suggestions, and encouragement :)
