---
layout: page
title:  "Particle Swarm Optimization"
subheadline:  'by Yubo "Paul" Yang'
teaser: "Particle Swarm Optimization (PSO) is a nature inspired optimization algorithm. PSO mimics the behavior of a flock of birds looking for food source."

categories:
    - algorithm
tags:
    - optimization
image:
   thumb: "yolo.png"
header:
    image_fullwidth: "pso_steps.png"
    caption: PSO optimization of the 2D Rastrigin function.
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * Motivation for PSO.
  * Show an example where the algorithm works well. (2D Rastrigin)
  * Modification needed to apply it to the bin packing problem.

## Examples
My pso example to minimize the 2D Rastrigin function [notebook][2] ([html][3]) and related [python library][4].

## References
  * Official [Tutorial][5]
  * Paper on [convergence criteria][6], [sign test][7]
  * Application to the [bin packing problem][8]

### All optimization.
{: .t60 }

{% include list-posts tag='optimization' %}

[1]: {{ site.url }}/assets/slides/particle_swarm_optimization.pdf
[2]: {{ site.url }}/assets/notebooks/pso_demo.ipnb
[3]: {{ site.url }}/assets/notebooks/pso_demo.html
[4]: {{ site.url }}/assets/notebooks/fmin_2dpso.py
[5]: http://www.swarmintelligence.org
[6]: http://dx.doi.org/10.1016/S0020-0190(02)00447-7
[7]: http://dx.doi.org/10.1109/CEC.2007.4424905
[8]: http://dx.doi.org/10.1016/j.ejor.2007.06.032
