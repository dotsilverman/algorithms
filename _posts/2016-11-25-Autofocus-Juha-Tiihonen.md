---
layout: page
title:  "Automatic focusing of cameras"
subheadline:  "by Juha Tiihonen"
teaser: "Autofocus is an essential feature in any optical imaging devices, such as cameras or microscopes. We go through the most common approaches for finding the optimal focus distance and demonstrate focus classification with several digital focus functions."

categories:
    - algorithm
tags:
    - optimization
    - imaging
    - optics
image:
   thumb: "autofocus_thumb.jpg"
header:
    image_fullwidth: "autofocus.jpg"
    caption: Automatic focusing gives you one extra hand in photography.
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * Introduction to the problems and algorithms involved with image focusing
  * Three different examples of digital focus functions
  * Demonstration of those focus functions on actual images


## Examples
Complete example including cropped image files and MATLAB scripts in ZIP archive: [notebook][2] 

## References
https://graphics.stanford.edu/courses/cs178/applets/autofocusPD.html
https://dx.doi.org/10.1002/cyto.a.22020
https://dx.doi.org/10.1109/TCSVT.2008.924105
https://dx.doi.org/10.1111/j.1365-2818.1988.tb04620.x

### All optimization.
{: .t60 }

{% include list-posts tag='optimization' %}

[1]: {{ site.url }}/assets/slides/autofocus.pdf
[2]: {{ site.url }}/assets/notebooks/autofocus_example.zip
