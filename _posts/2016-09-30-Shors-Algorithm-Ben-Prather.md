---
layout: page
title:  "Shor's Algorithm"
subheadline:  'by Ben Prather'
teaser: "An informal description of Shor's algorithm for factorization by a quantum computer."

categories:
    - algorithm
tags:
    - quantum algorithms
    - factorization
    - number theory
image:
   thumb: "ShorSum.png"
header:
    image_fullwidth: "ShorSum.png"
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I go over the two basic components of Shor's algorithm:

* The number theory required to reduce the factorization problem to a period-finding problem
* The quantum fourier transform, which finds the period of a function in polynomial time

## References

* Several more comprehensive descriptions of the algorithm are listed on the last slide

### All Quantum Computing
{: .t60 }

{% include list-posts tag='quantum algorithm' %}

[1]: {{ site.url }}/assets/slides/Shors.pdf
