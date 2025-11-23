---
layout: post
title: Struct of Arrays (SoA) vs Array of Structs (AoS) in Python
date: 2025-11-23 19:54:16 +0100
tags: [projects]
excerpt: I benchmarked SoA vs AoS in Python. While SoA was more efficient than AoS, its readability penalty outweighed the gains.
published: true
---
I am looking into ways to accelerate my artificial-life code (~1,000 agents, each running a small `PyTorch` neural network). Gemini 2.5 Pro suggested two things: using Struct of Arrays (SoA) instead of Array of Structs (AoS) in Python, and using `JAX` with `jit` and `vmap` instead of `PyTorch`.

This is a benchmark I wrote to understand the performance gains of the first proposal.

What are Struct of Arrays (SoA) and Array of Structs (AoS)?

Array of Structs (AoS) example:
```python
points = [
    {"x": 1, "y": 2},
    {"x": 3, "y": 4},
]
```

Struct of Arrays (SoA) example:
```python
x = [1, 3]
y = [2, 4]
```

The idea, as I understand it, is: when iterating over large arrays, similar fields should be stored contiguously to make better use of the CPU cache.

I tried two experiments: first, operations between `X` and `Y`; second, operations between two elements within `X`. I tested different data structures (NumPy arrays, Python lists, and classes with __slots__).

The results confirmed that SoA is faster than AoS. The benchmark below shows timings in seconds for 10 million accesses (randomly selected indices) on 10‑million‑element arrays:

```
# Data Structure            XY Operation Time (s)     XX Operation Time (s)
# ---------------------------------------------------------------------------
# AoS                       9.04847                   8.78820
# SoA                       5.33116                   5.61287
```

However, the improvement is marginal for my use case. I don't care much about a 3–4 second difference after 10 million accesses, and the SoA representation is less readable than AoS.

**Conclusion**: I’m continuing with AoS. I may revisit this when I’m operating at billions of accesses on a regular basis.

Full benchmark code:
<script src="https://gist.github.com/osm3000/f06e837951df8ed9c3cd8ec43c5c5673.js"></script>