---
layout: page
title:  "Automatic Differentiation"
subheadline:  "by Yubo \"Paul\" Yang"
teaser: "Automatic Differentiation exploits the fact that any algebraic function implemented on a computer can be compiled into a long list of elementary operations and elementary functions. Using this observation, exact differentiation can be carried out exactly by exploiting the chain rule."
categories:
    - algorithm
tags:
    - automatic differentiation
    - numerical method
image:
   thumb: "ad-thumb.png"
header:
    image_fullwidth: "TRW_StateEstimation.png"
    caption: from NeoFortran semantics
    caption_url: http://fortranwiki.org/fortran/show/NeoFortran+semantics
---
<!-- Page Content -->


## Presentation Slides
[link][1] to pdf 

## Jupyter Notebook
[link][2] to notebook

## References
* Relation to [Apollo][3]
* [Tutorial][4] by Prof. Tamas Terlaky from McMaster Univeristy
* [Demonstration][5] by Boyana Norris at Argonne with many applications
* Dedicated [topic website][6] established by Argonne staff

## All Numerical Methods
{: .t60 }

{% include list-posts tag='numerical method' %}

[1]: {{ site.url }}/assets/slides/KalmanFilter.pdf
[2]: {{ site.url }}/assets/notebooks/KalmanFilter.ipynb
[3]: http://www.metacalculus.com/apollo.html
[4]: http://www.cas.mcmaster.ca/~cs777/presentations/AD.pdf
[5]: http://science.energy.gov/~/media/ascr/ascac/pdf/meetings/nov10/Norris.pdf
[6]: http://www.autodiff.org/
