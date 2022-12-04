---
layout: page
title: Photometric Redshifts
description: Techniques and Data Products
img: assets/img/weave.png
importance: 3
category: techniques
---

Photometric redshifts (or photo-z's) are a critical tool in both 


### All-purpose, all-sky redshifts

I recently produced photo-z estimates for the Dark Energy Spectroscopic Instrument (DESI) Legacy Imaging Surveys, currently the most sensitive optical survey covering the majority of the extragalactic sky - published in MNRAS: [Duncan (2022)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.3662D/abstract).

My photo-z methodology was based on a machine-learning approach, using sparse Gaussian processes augmented with Gaussian mixture models (GMMs) that allow regions of parameter space to be identified and trained separately in a purely data-driven way. The same GMMs are also used to calculate cost-sensitive learning weights that mitigate biases in the spectroscopic training sample. 
By design, this approach aims to produce reliable and unbiased predictions for all parts of the parameter space present in wide area surveys. Compared to previous literature estimates using the same underlying photometry, my photo-z's are significantly less biased and more accurate at $$z > 1$$, with negligible loss in precision or reliability for resolved galaxies at $$z < 1$$. 
The estimates offer accurate predictions for rare high-value populations within the parent sample, including optically selected quasars at the highest redshifts ($$z > 6$$), as well as X-ray or radio continuum selected populations across a broad range of flux (densities) and redshift. Deriving photo-z estimates for the full Legacy Imaging Surveys Data Release 8, the catalogues provided in this work offer photo-z estimates predicted to be of high quality for $$9\times10^8$$ galaxies over $$∼19\,400 \text{deg}^2$$ and spanning $$0<z<7$$, offering one of the most extensive samples of redshift estimates ever produced.


- [CosmosHub (registration required)](https://cosmohub.pic.es/catalogs/291): This database allows easy queries based on source position and properties  join directly with the photometry that is not included in my catalogues to save space (an account required).

Flat files can also be found on U.Edinburgh’s repository here:
https://datashare.ed.ac.uk/handle/10283/4420

### LOFAR Two-meter Sky Survey Data Releases
