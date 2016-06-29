---
layout: page
title:  "Introduction to Supervised Machine Learning"
subheadline:  "by Benjamin Villalonga Correa"
teaser: "With Supervised Machine Learning techniques we can train a model to "

categories:
    - algorithm
tags:
    - artificial intelligence
    - machine learning
    - supervised machine learning
    - neural networks
image:
   thumb: "ad_thumb.png"
header:
    image_fullwidth: "compressed_sensing_lana.jpg"
    caption: from Phys. Rev. X 2, 021005 (2012)
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * the basic problem this solves.
  * why it makes sense to optimize for scarsity.
  * results from my own implementation of the l-1 minimization approach.
  * an exploration of the parameter space for which this method is successful.
  * recent developments in the field, and it's connection to physics.


## Examples
My compressed sensing [notebook][2] ([html][4]) and related [python library][3].

## References
Original paper (I think? in some sense?):

 IEEE Trans. Inf. Theory **52**, 1289 (2006)

Probabilistic seeding: 

Phys. Rev. X **2**, 021005 (2012)

Simultaneous measurement of physical observables.: 

Phys. Rev. Lett. **112**, 253602 (2014)

### All signal processing.
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]: {{ site.url }}/assets/slides/compressed_sensing.pdf
[2]: {{ site.url }}/assets/notebooks/compressed_sensing.ipynb
[3]: {{ site.url }}/assets/notebooks/compressed_sensing.py
[4]: {{ site.url }}/assets/notebooks/compressed_sensing.html

