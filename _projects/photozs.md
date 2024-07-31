---
layout: page
title: Photometric Redshifts
description: Techniques and Data Products
img: assets/img/weave.png
importance: 3
category: techniques
---

Photometric redshifts (or photo-z's) are a critical tool in both galaxy evolution studies and cosmological probes.


## All-purpose, all-sky redshifts

I recently produced photo-z estimates for the Dark Energy Spectroscopic Instrument (DESI) Legacy Imaging Surveys, currently the most sensitive optical survey covering the majority of the extragalactic sky - published in MNRAS: [Duncan (2022)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.3662D/abstract).

My photo-z methodology was based on a machine-learning approach, using sparse Gaussian processes augmented with Gaussian mixture models (GMMs) that allow regions of parameter space to be identified and trained separately in a purely data-driven way. The same GMMs are also used to calculate cost-sensitive learning weights that mitigate biases in the spectroscopic training sample. 
By design, this approach aims to produce reliable and unbiased predictions for all parts of the parameter space present in wide area surveys. Compared to previous literature estimates using the same underlying photometry, my photo-z's are significantly less biased and more accurate at $$z > 1$$, with negligible loss in precision or reliability for resolved galaxies at $$z < 1$$. 
The estimates offer accurate predictions for rare high-value populations within the parent sample, including optically selected quasars at the highest redshifts ($$z > 6$$), as well as X-ray or radio continuum selected populations across a broad range of flux (densities) and redshift. Deriving photo-z estimates for the full Legacy Imaging Surveys Data Release 8, the catalogues provided in this work offer photo-z estimates predicted to be of high quality for $$9\times10^8$$ galaxies over $$∼19\,400 \text{deg}^2$$ and spanning $$0<z<7$$, offering one of the most extensive samples of redshift estimates ever produced.

The full catalogues are available through a range of services and formats:
- [CosmosHub (registration required)](https://cosmohub.pic.es/catalogs/291): This database allows easy queries based on source position and properties  join directly with the photometry that is not included in my catalogues to save space (an account required).
- [Vizier](https://cdsarc.cds.unistra.fr/viz-bin/cat/VII/292)
- Flat files can also be found on U.Edinburgh’s [DataShare](https://datashare.ed.ac.uk/handle/10283/4420)
repository.

## LOFAR Two-meter Sky Survey Data Releases

I have worked extensively on the development of photo-z techniques for the LOFAR Two-meter Sky Survey (LoTSS), the deepest low-frequency radio continuum survey to date. 
In addition to the work outline above which provides redshift estimates for the LoTSS 2nd Data Release (DR2), I have also produced photo-z estimates for the [LoTSS 1st Data Release (DR1)]() and the [LoTSS Deep Fields (LDFs)](https://lofar-surveys.org/deepfields.html) that are publicly available through the LOFAR Surveys Key Science Project [website](https://lofar-surveys.org/).

The associated techniques and data release papers for all this work can be found on my [Publications](/publications) page.

## GPz_Pype

The Gaussian Mixture Model augmented Gaussian Process (GPz) photo-z code I developed for the DESI Legacy Imaging Surveys is currently in the process of being repackaged as a self-consistent and flexible Python package, [GPz_Pype](https://dunkenj.github.io/gpz_pype/).
The package is designed to be easy to use and flexible, allowing users to easily train and test their own GPz photo-z models on their own data while incorporating the benefits of the GMM augmentation and cost-sensitive learning techniques I developed for [Duncan (2022)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.3662D/abstract).

__Note:__ The package is still in development and is not yet ready for widespread release. Please follow on GitHub for updates or email me if you are interested in using the package.