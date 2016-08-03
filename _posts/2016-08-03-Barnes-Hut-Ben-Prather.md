---
layout: page
title:  "The Barnes-Hut Algorithm"
subheadline:  "by Ben Prather"
teaser: "The Barnes-Hut algorithm approximately solves the N-body problem using only O(N log(N)) time"

categories:
    - algorithm
tags:
    - n-body astrophysics
image:
   thumb: "barnes_hut_small.png"
header:
    image_fullwidth: "barnes_hut.png"
    caption: Partitioned 2D Ensemble
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I give an overview of the Barnes-Hut algorithm, an optimization of the usual solution to the N-body problem at the cost of some accuracy.  It works by approximating far-away clusters of objects as single, larger objects.

## References
* [Original Paper](http://www.nature.com/nature/journal/v324/n6096/abs/324446a0.html): Barnes & Hut, “A hierarchical O(N log N) force-calculation algorithm,” Nature 324, 446 - 449 (04 December 1986); doi:10.1038/324446a0
* Parallel examples: [Scala](https://scala-blitz.github.io/home/documentation/examples//barneshut.html), [Other](http://ta.twi.tudelft.nl/PA/onderwijs/week13-14/Nbody.html)
* [Gravitational interaction speed](https://arxiv.org/abs/gr-qc/9909087)
* Notable N-body simulations: [Bolshoi](http://hipacc.ucsc.edu/Bolshoi/), [Millennium](http://wwwmpa.mpa-garching.mpg.de/millennium/)
* Björk concert: "[Dark Matter](https://www.youtube.com/watch?v=dkagu0qWBio)," Bestival 2011


{: .t60 }

{% include list-posts tag='astrophysics' %}

[1]: {{ site.url }}/assets/slides/barnes_hut.pdf
