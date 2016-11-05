---
layout: page
title:  "Pitch Correction"
subheadline:  "by Benjamin Villalonga Correa"
teaser: "Pitch correction is widely used in the music industry both in real time and in post-production situations. Depending on the original quality of an artist, pitch correcting techniques can range from allowing an already good performance to become excellent (as far as tuning is concerned) to making a terrible one sound robotic and surprisingly late-90-ish. From an engineering point of view, the difficulty of these algorithms boils down to being able to manipulate independently time scales and frequencies in a signal. One algorithm that achieves this is the Phase Vocoder, which is discussed in this presentation. Its range of application goes beyond pitch correcting purposes, so more insight in the kind of problems that it tackles will also be given. An example of the commercial software Auto-Tune is also linked."

categories:
    - algorithm
tags:
    - signal processing
    - music
    - auto-tune
image:
   thumb: "backstreet_boys.jpg"
header:
    image_fullwidth: "singing.jpeg"
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I talk about:

  * the pitch-correction problem.
  * the Phase Vocoder algorithm.
  * other applications of the Phase Vocoder algorithm.
  * an example using Auto-Tune.


## Examples
  * Auto-Tune example in [this youtube video][2].

## References
  * A good intuitive [explanation][3].
  * Short accessible [paper][4].
  * More rigorous, still accessible [paper][5].
  * Long and complete scientific [paper][6].

### All Signal Processing.
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]: {{ site.url }}/assets/slides/pitch-correction.pdf
[2]: https://www.youtube.com/watch?v=6fTh0WRJoX4
[3]: http://blogs.zynaptiq.com/bernsee/pitch-shifting-using-the-ft/
[4]: http://dave.ucsc.edu/physics195/thesis_2009/m_peimani.pdf
[5]: http://music.informatics.indiana.edu/media/students/kyung/kyung_paper.pdf
[6]: http://chamilo2.grenet.fr/inp/courses/PHELMAA35PMSPAR0/document/Projet_TFN/MoulinesLaroche1995.pdf

