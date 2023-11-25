---
layout: post
title:  "Reflections on learning programming"
date:   2023-10-27 00:00:00 +0200
categories: thinking
tags: [programming, reflection]
published: true
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

So, a similar course, but from Princeton, was starting. I was determined to get it right this time. First week was brutal, I struggled a lot. Second week, I was working day and night, I simply couldn't finish. There was this shocking realization that...I am not good at programming in the first place.

With humiliating idea in my mind, I searched for a 101 programming course. I ended up with MITx 6.00.1x (and afterwords 6.00.2x), which was wonderful by all standards, and also my first introduction to `python`. Heavy course, but it set strong foundations, that ended up being very useful later on.

## Flourishing (2015 - 2019)
During the MSc, internships, and Phd, I wrote a lot of programs. Through these many iterations, my level (and comfort with writing code) improved rapidly, whether in terms of speed, quality or abstractions. My focus was on scientific experiments or data analysis during this period.

Quantity was important. Quantity led to emergent of quality.

Just to be clear, by any industry standards, my code quality was still very low (shocking realization that I had to face during interviews).

Something also that struck me is that discussing the coding with others led to rapid feedback, and hints here and there, that accelerated the learning and the improvement process rapidly.

Most of the code that I wrote though was being used by me only, for few times. This is things with scientific experiments: you don't necessarily have a clear vision of what the problem is going to be, so it is hard to imagine an architecture that will be useful in the long run, thus, you end up writing a lot of "disposable" code.

But there is an important lesson here that I always carried with me: just go for it. Iterations are unavoidable, and perfection from the first time is a myth. While I still cherish this value, it led to a lot of bad impressions later on in life: people will always judge from the first iteration.

The exposure that I had to other technologies was very limited: I didn't know anything about databases. `git` was counter-intuitive to me. I couldn't build a dynamic website, or knew anything about the web (except HTML perhaps?) or networks. With such amount of disposable code, writing tests was like discussing science fiction.

## The industry (2020 - ...)

In 2020, I started my second startup, as part of "Entrepreneur First" program. I was the CTO. A friend of my co-founder, Max, joined us. A veteran software engineer, with a lot of experience in the industry. The whole things lasted for 3 months. We deployed a couple of prototypes with customers. I've learned A LOT from Max. He was a very humble, down-to-earth person. He took the time to explain the basics of the basics to me.

It was the first time I "deploy" something, the first time anyone is using my work. It felt really great! (and I still get this feeling to this day when people are using my work).

During this period, one my roommates, Dom, was on an accelerated path of self-improvement to become a software engineer. We had a lot of discussions, and this led to rapid improvement on my side as well.

From the continuous "issues" during the interviews, it was clear that I need to do a lot of conscious effort to improve my "first" outcome when I write code. The problem was, coming from a scientific background, is that I don't have any clear patterns in my mind (since, as I explained earlier, the problem is not clear most of the time in science, and a lot of the code is disposable). 

This is not the case in industry though: the problems do evolve for sure, but somehow, the patterns are the same. And when you start a new work, there is a "right way" of doing things. Granted, there are opinions here, but enumerable. Going out of those ways/patterns seemed to always raise a red flag to the person viewing the code. 

It took a while to understand that, and with trial-and-error, and lots of good advice and informative discussions, I finally started converging to these patterns, and the first iteration of my code started to look better and better.

All the elements that didn't make sense to more started to fell into place: git, database, workflows, testing, ...etc. I still have a lot to learn, but I am getting there. And now I am going more towards system design, distributed systems, and cloud architecture.

## Conclusion

I've always compared myself to those hackers in "Hackers: Heroes of the Computer Revolution" book, or others that I was reading about all the time. I always felt really terrible about myself, and always super frustrated. I felt terrible for not being of a good-enough nationality, or having the right environment and resources. Getting to where I am at this moment was a very long and painful journey.

What if I had a coach? What if I natively spoke English? What if I had a chance to go to MIT? 

Yet, in reflection, this self-torture never bare any fruits. There was no difference in outcome between this and being optimistic, relaxed, and enjoying the process. This doesn't negate the important of being attentive, working hard, and seeking the opportunities. 

I am more at peace now. I just hope that, for those who are facing similar situations like I had back in the day: work hard, be flexible, but don't hate yourself. There are things that you can control, but there are things that you can't. Don't settle, but don't torture yourself either.