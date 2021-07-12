---
title: 'mednoise: a python package for medical image processing'
tags:
  - Python
  - medicine
  - bioinformatics
  - imaging
  - machine learning
authors:
  - name: Ravi Bandaru
    orcid: https://orcid.org/0000-0001-7109-9894
    affiliation: 1
affiliations:
 - name: Cincinnati Children's Hospital - Division of Human Genetics
   index: 1
   
date: 12 July 2020
bibliography: paper.bib
---

# Summary

`mednoise` is a library for processing medical images in Python. It contains various algorithms which are highly tuneable, enabling it to encompass a wide variety of scientific use-cases. The algorithms contained in mednoise are grounded in `NumPy` arrays. mednoise treats each image as a two-dimensional array of pixels which is processed with a variety of manipulations and substitutions. 

When given a series of medical images, mednoise runs user-requested computations, eventually yielding a final medical image, without noise, that is primed to be analyzed by machine learning and deep learning models.

These noiseless images improve the accuracy of AI imaging models, both supervised and unsupervised, significantly. mednoise offers an easy-to-use terminal interface while processing medical images. Additionally, its inference-compatible nature allows for easy integration into existing scientific workflows, like `Luigi, Airflow`, and `Snakemake`. By processing and outputting medical images that heavily improve image-specific AI models, `mednoise` facilitates high-speed scientific model creation and image analysis.

# Statement of need

With the field of artificial intelligence and bioinformatics growing almost exponentially, programming languages have adapted to include more machine learning and deep learning libraries. Within Python, there are `TensorFlow` and `SciKit-Learn`, modules that offer the ability for users to develop AI models with minimal keystrokes.

The field of medical imaging, however, has not adapted with similar speed. Medical imaging tools used in medical offices across the world are rarely new and are not optimized for modern AI models.

Enter `mednoise`, an easily integrable tool designed entirely in Python, to process medical image metadata into usable formats for machine learning models.

More specifically, mednoise removes unnecessary noise that has unremarkable clinical significance, yielding medical images that have the highest impact possible in bioinformatics research.

The design of mednoise lends the package immense potential. mednoise can be easily integrated into any workflow, high-performance computing network, and even medical imaging tools themselves. With its open and highly tuneable structure, this package is useful to almost any usecase related to medical image research.

mednoise is designed as a tool for pipelines and workflow management systems that rely on medical image metadata (or at least the analysis of that metadata). It aims to create a future of medical imaging that is more accessible and utilizable in the constantly evolving field of medical technology.

# Example
The following example demonstrates the processing of an ultrasound image with `mednoise`, specifically its `branch` algorithm. The example
makes use of the example image, hosted on the documentation website, that is provided for generation of reproducible bug reports. 
```python
  >>> from mednoise import branch as md
  >>> md.branch_complete("/example/directory/file.PNG", 450, 350, 500) #file.PNG contains example image from mednoise.github.io/exampleimage.html
  md.branch_complete - Image 1 Importing:0:00:01
  md.branch_complete - Image 1 Converting:0:00:00
  md.branch_complete - Image 1 Translating:0:00:00
  md.branch_complete - Image 1 Branching:0:42:04
  md.branch_complete - Image 1 Branch Analyzing:0:03:02
  md.branch_complete - Image 1 Branch Isolating:0:00:10
  md.branch_complete - Image 1 Array Priming:0:00:00
  md.branch_complete - Image 1 Translating:0:00:00
  md.branch_complete - Image 1 Saving:0:00:01
```
# Overview

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
