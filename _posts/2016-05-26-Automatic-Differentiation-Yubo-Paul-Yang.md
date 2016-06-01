---
layout: page
title:  "Automatic Differentiation"
subheadline:  "by Yubo \"Paul\" Yang"
teaser: "Automatic Differentiation exploits the fact that any algebraic function implemented on a computer can be compiled into a long list of elementary operations and elementary functions. Using this observation, exact differentiation can be carried out efficiently by exploiting the chain rule."
categories:
    - algorithm
tags:
    - automatic differentiation
    - numerical method
image:
   thumb: "ad_thumb.png"
header:
    image_fullwidth: "TRW_StateEstimation.png"
    caption: from NeoFortran semantics
    caption_url: http://fortranwiki.org/fortran/show/NeoFortran+semantics
---
<!-- Page Content -->


## Presentation Summary
[link][1] to pdf 

## Examples
[link][2] to notebook
compute graph generation [example][8]
source code transformation (SCT) [example][9]

## Active Researcher
[Sebastian F. Walter][7]

| Package | Description | Last Commit |
| ------- |:----------- | -----------:|
| algopy  | native python ad, work with numpy | Jun 30, 2015 |
| pyadolc | wrapper for ADOL-C (C++) | Mar 30, 2016 |
| pycppad | wrapper for CppAD | July 10, 2014 |

## References
* Relation to [Apollo][3]
* [Tutorial][4] by Prof. Tamas Terlaky from McMaster Univeristy
* [Demonstration][5] by Boyana Norris at Argonne with many applications
* Dedicated [topic website][6] established by Argonne staff

### All Numerical Methods
{: .t60 }

{% include list-posts tag='numerical method' %}

[1]: {{ site.url }}/assets/slides/KalmanFilter.pdf
[2]: {{ site.url }}/assets/notebooks/KalmanFilter.ipynb
[3]: http://www.metacalculus.com/apollo.html
[4]: http://www.cas.mcmaster.ca/~cs777/presentations/AD.pdf
[5]: http://science.energy.gov/~/media/ascr/ascac/pdf/meetings/nov10/Norris.pdf
[6]: http://www.autodiff.org/
[7]: http://expdesign.iwr.uni-heidelberg.de/people/swalter/index.html
[8]: {{ site.url }}/assets/notebooks/ad_algopy_reverse.ipynb
[9]: {{ site.url }}/assets/notebooks/ad_sct.ipynb
