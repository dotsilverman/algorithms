---
layout: page
title:  "Adaptive Boosting (AdaBoost)"
subheadline:  "by Matt Zhang"
teaser: "AdaBoost is a systemmatic way to construct a complicated model (strong learner) by combining many copies of a simple model (weak learner). Each simple model is fit to a reweighted data set, where unexplained data have higher weights."

categories:
    - algorithm
tags:
    - machine learning 
image:
   thumb: "rocket.jpg"
header:
    image_fullwidth: "adaboost.png"
    caption: from slides
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * adaptive boosting

## Examples
You imagine it

## References
* [Explaining AdaBoost][2] by Robert E. Schapire
* [Example][3] usage with BDF
* [Comparison][4] with other algorithms
* [How Boosting the Margin can Also Boost Classifier Complexity][5] by Reyzin and Schapire

### All Machine Learning
{: .t60 }

{% include list-posts tag='machine learning' %}

[1]: {{ site.url }}/assets/slides/AdaBoost.pdf
[2]: http://rob.schapire.net/papers/explaining-adaboost.pdf
[3]: https://indico.scc.kit.edu/indico/event/48/session/4/contribution/35/material/slides/0.pdf
[4]: http://www.37steps.com/exam/adaboost_comp/html/adaboost_comp.html
[5]: http://www.levreyzin.com/presentations/ReyzinSch06_icml_presentation.pdf
