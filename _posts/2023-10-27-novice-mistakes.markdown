---
layout: post
title:  "Reflections on Programming"
date:   2023-10-27 00:00:00 +0200
categories: thinking
---

There is a deep love that is hard to understand or express: the simplicity and purity of the relationship, sound of keyboard, the feeling of control, the gratification of the outcome, the challenge of the puzzle, the room for improvement, the patience of the machine...

I have been programming for more than 20 years, and I still feel like a novice. I still feel like I am learning the basics. I still feel like I am learning how to learn. I still feel like I am learning how to think.

This is merely a reflection on an activity I deeply love and cherish.

## Young dreams (? - 2003)
I was dreaming about coding. I really liked the idea of having a conversation with the machine: It felt like a mix of gratification of control, and the honesty of the feedback. I was reading stories about hackers and programmers, but it felt very unclear how to reach that, or where to start.

## Troublesome beginnings (2003 - 2008)
I managed to put my hands on a arabic book on `Visual Basic 6`, which was really exciting. But,...where is visual basic exactly? 
I was already pretty good with Microsoft word at that time. Unfortunately, it was offering some sort of `visual basic` macros - if my memory serves me right -. For a while, I thought this is where Visual Basic is. I tried a lot to make it work, but it didn't. I was very disappointed.

It is important to understand the context here: I couldn't read in English back then. The resources in Arabic was really scarce. There was no community or anyone to talk to. I was new to the internet, but what can be done with the internet was still work in progress. There were no libraries you just go to in order to buy book. 

Then, a breakthrough happened in 2003: a colleague in my class happened to have been programming for a while (the first and last person I meet during my school years who did any programming). He gave me a copy of `Microsoft Visual Studio 6`, and Voila!! I was in.
But with this amazing gift came a bad curse: he advised me to change to `C++` instead, since it is a much more powerful language. And I didn't waste any time: I set sail to `C++`.

One of the first books I picked was `C++ in 21 days`. I decided that English is the way to go. I spent over 6 months, progressing 1 page a day, translating word by word, just to realize that the sentence doesn't mean much to me. My dad also believed in using a traditional dictionary instead of an electronic one, which made the process even more painful. I was really struggling, but I was determined to make it work. And it worked.

I also found a couple of other books in arabic. One book, the deeply touched me, was for a Saudi engineer (I can't for the life of me find any traces of him). At that time, pirated books was the only available way. However, that guy put his book online for free, and asked that if you like his book, to buy it. It was such a revolutionary idea, I was really touched by it. I never knew how to buy the book though. I would still love to buy it.

With English unlocked, and these few precious arabic resources, rapid progress was made: I could do all the basic things in `C++`. I can't count how many times I built a calculator. 

But then what? Here was the curse. I actually didn't know what to do. My fantasies when I started programming was hacking mainly and building games. Now, what do I do with that syntax?
The road to making simple games was probably more feasible with `Visual Basic`, but the wall was pretty damn high with `C++` (I didn't realize it that time). 
My solution was: study more books about `C++`. Not very long after, my advance has stagnated, and I was stuck.

## The first breakthrough (2008 - 2010)
I took an electronics course in the summer of 2008, where we learned to program micro-controllers. I was already familiar with the `C` language, which made this part of the course easy for me, but most importantly, it gave me a meaning: I can write a piece of code that will turn a LED on and off! It was a crazy powerful idea! I can...do things! And it was not far fetched to imagine doing useful things to me.

After that course, I built a lot of small programs for micro-controllers, went for multiple large projects (robots mainly). It was fun and painful in the same time Working with micro-controllers means working with hardware, which is a tough cookie though: it is expensive, and debugging is hard. But it was a lot of fun.

I took a course on `assembly` for `x86` back then, which was oddly satisfying. It did reinforce a certain idea that was building up: I like working close to the metal. High levels of abstraction didn't appeal to me that much.

## The second breakthrough (2011 - 2013)
Necessity dictated that I put an end to my projects with micro-controllers: 

- They were expensive, and I personally couldn't afford the electronics part
- I loved mixing electronics was mechanics, which was far more expensive and complex. 
    - I was already suffering from multiple failures in orchestrating projects with people from mechanical engineering.
- There were barely any electronics in Egypt: sensors, motors, wireless modules, etc. were very hard, if not completely unavailable, to find. 
- A multimeter will only get you so far. Without access to an oscilloscope, debugging was a nightmare.

It was survival time. Thanks to the strategic insight from a dear friend (Moustafa Kassem), we started working on a project on FPGA. I shifted to `Verilog`, which is a language to describe hardware elements and the connections between them. The beauty of the setup at the time was that it removed all complex elements: access to hardware wasn't required for the vast majority of the time, and simulators would do just fine. 

I loved `verilog`, the setup, everything related to computer architecture, but the projects were not fun at all. They were...the right and responsible thing to do. I tried to find fun in pockets inside the projects (architecture, module design, code quality, etc.), but it was not the same. My heart was not in it.

One interesting thing during those years is that I still didn't understand most of the concepts that student in computer engineering were taught in programming courses. For me, everything was a `Finite State Machine`.

Doing the right things though paid off very well: I got a couple of very lucrative jobs offers before I graduated. 

My work in Siemens was a continuation of these projects. It was stimulating to see high quality code and patterns from more experienced engineers. I learned a lot.

But then, I stumbled upon this weird language: `Perl`, which was used to build parsers, as part of our verification environment. I damn loved `Perl` and `regular expressions`. I read a couple of books, did so many small programs. I was pretty good at reading all this alien-like notations. 

But, most importantly, I had use-cases: automating parts of my work.

For example, when we run the regressions test-cases, we needed to fill an excel sheet with the results of each test-case. And boy I sucked at this! So, I wrote a script that would parse the log files, and fill the excel sheet for me, with colors and stats and everything. It was amazing! I was hooked.
I built a system to generate more complex test-cases (back then, we were writing the test-cases manually, following an agreed upon verification plan). Found 3 critical bugs before the release. Neat! The project manager was very happy, and he presented it to the department director. It was awesome!

`Perl` was just the right level of abstraction, in the right time, with the right problems. I love it to this day.

My love for `verilog` fading away. I always wanted to build a microprocessor. I found that book about a demonstration processor called `Vespa`

Back then, I read a couple of books that had a great impact on me:
- `Automate this: How algorithms came to rule our world`
- `The Age of Spiritual Machines: When Computers Exceed Human Intelligence`

This encouraged me to do *Andrew Ng*'s famous course on *Machine Learning*

## Hard reset (2014)
I started a MSc in embedded systems in Switzerland, but two months in, it was clear that my heart and mind is in Artificial Intelligence. I applied for another MSc in France, in ML, got accepted.
There were ~6 months until I started the MSc. Since I don't come from a CS background, and my math (statistics in particular) wasn't up to the task, I decided to take the time to invest in online courses, address my weak points, and prepare for the MSc.

One course in particular I tried to do many times a year earlier, and failed consistently, was Algorithms course from Stanford. Every time I made an excuse: I was too busy, the stars were not aligned, ...etc.
This time, I was adamant to get it right. I even blamed the course itself.
So, a similar course, but from Princeton, was starting. I was determined to get it right this time. First week was brutal, I struggled a lot. Second week, I was working day and night, I simply couldn't finish.

There was this shocking realization that...I am not good at programming in the first place. 