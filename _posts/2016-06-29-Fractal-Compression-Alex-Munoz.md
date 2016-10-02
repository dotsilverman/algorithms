---
layout: page
title:  "Fractal Compression"
subheadline:  "by Alex Munoz"
teaser: "Fractal compression uses self-similarity in images and functions to reduce the redundant content. This technique takes redundancies and stores them as affine transformations with a set of coordinates."

image:
   thumb: "SierpinskiDreieck.png"
header:
    image_fullwidth: "Mandelbrot.jpg"
    caption: the Mandelbrot set from Wikipedia

categories:
    - algorithm
tags:
    - compression
    - fractals
    - signal processing

---
<!-- Page Content Starts Here -->

## Presentation Summary
In my [presentation][1], I talk about:

  * the necessary mathematics for fractal image compression.
  * how the algorithm stores information.
  * the implementation of the algorithm.
  * possible applications.
  
## Examples
  * Basic [example][2], [htlm view][3]
 
## References
  * I will move references from my presentation to here soon!

### All signal processing.
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]: {{ site.url }}/assets/slides/FractalComp.pdf
[2]: {{ site.url }}/assets/notebooks/fraccomp.ipynb
[3]: {{ site.url }}/assets/notebooks/fraccomp.html
