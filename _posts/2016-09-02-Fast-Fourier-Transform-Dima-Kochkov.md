---
layout: page
title:  "Fast Fourier Transform"
subheadline:  "by Dima Kochkov"
teaser: "O(N log(N)) computation of a discrete fourier transform, fast integer multiplication"

categories:
    - algorithm
tags:
    - FFT
image:
    thumb: Fourier.jpg
header:
    image_fullwidth: "fourier.jpg"
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I will give a short overview of the Fast Fourier transform algorithm. We will look into different polynomial representations and corresponding computational complexities of simple algebraic operations. The FFT algorithm will gain it's performance by utilizing the coefficient and point-sample representations as well as an algorithm to compute one given the other.

## References
*"[MIT video lecture on FFT](https://www.youtube.com/watch?v=iTMn0Kt18tg)," by Erik Demaine

*"[lecture on FFT complexity analysis](http://www.cs.columbia.edu/~stratos/research/fft.pdf)"



{: .t60 }

{% include list-posts tag='FFT' %}

[1]: {{ site.url }}/assets/slides/FastFourierTransform.pdf
