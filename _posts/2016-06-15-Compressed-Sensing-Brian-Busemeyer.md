---
layout: page
title:  "Compressed sensing"
subheadline:  "by Brian Busemeyer"
Description: "Compressed sensing is a way of extracting a full signal out of a sparse sampling. It's only requirement is that the signal has a sparse representation in some basis, which is actually true for most interesting signals that we encounter."

categories:
    - algorithm
tags:
    - signal processing
    - numerical method
image:
   thumb: "cat_fourier.eps"
header:
    image_fullwidth: "compressed_sensing_lana.jpg"
    caption: from Phys. Rev. X **2**, 021005 (2012)
---
<!-- Page Content Starts Here -->

## Presentation Summary
Compressed sensing is a way of extracting a full signal out of a sparse sampling. 
It's only requirement is that the signal has a sparse representation in some basis, which is actually true for most interesting signals that we encounter. [link][1]


## Examples
* My compressed sensing [notebook][2] and related [python library][3].

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

