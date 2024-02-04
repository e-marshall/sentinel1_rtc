# Introduction 

This tutorial will demonstrate various ways to access, process, and work with Sentinel-1 Synthetic Aperture Radar (SAR) Radiometrically Terrain Corrected (RTC) imagery using the python package and open source project [xarray](https://docs.xarray.dev/en/stable/#), and a number of other open-source software packages. These notebooks are designed to show examples of data access, manipulation, processing, and exploratory analytical workflows with complex datasets and demonstrate common functionality for working with multi-dimensional gridded data using xarray.

# Overview

This tutorial contains a number of jupyter notebooks that focus on working with Sentinel-1 imagery that has already undergone Radiometric Terrain Correction (RTC). Because SAR imagery is collected from a side-looking sensor, it can contain distortions related to the viewing geometry of the sensor and the surface topography of the area being imaged. 

SAR data is collected in slant range, which is the viewing geometry of the side-looking sensor and has two dimensions: range and azimuth. These are the along-track and across-track directions of the imaged swath. As data is transformed from radar coordinates (slant range) to geocoded coordinates, the spaces represented by individual pixels in the two coordinate systems do not always align, and distortions can arise due to certain viewing angle geometries and surface topography features. In addition, radiometric distortion can arise due to scattering responses from multiple scattering features within a single pixel. Radiometric terrain correction is a processing step that accounts for these distortions and the transformation from radar to geocoded coordinates that prepares SAR data for analysis. For a much more detailed explanation of this, check out the Alaska Satellite Facility (ASF) [product guide for RTC imagery](https://hyp3-docs.asf.alaska.edu/guides/rtc_product_guide/). Chapter 2 of the [SAR Handbook](https://gis1.servirglobal.net/TrainingMaterials/SAR/Chp2Content.pdf) also has very useful descriptions of these concepts. 

Multiple algorithms perform radiometric terrain correction, and it is important to understand the components of whichever dataset you use and their relative benefits and tradeoffs. This book will demonstrate working with two different (but similar) datasets of Sentinel-1 RTC imagery. Processing of SAR imagery can be very computationally intensive, so we focus on datasets that leverage cloud-computing resources, including both cloud-processed and cloud-hosted data, as well as data that is processed in the cloud and then downloaded locally. 

# Learning objectives

This tutorial demonstrates accessing and working with different Sentinel-1 SAR RTC datasets. The learning goals include **domain-specific steps related to working with synthetic aperture radar data** and specific *python and xarray techniques*. 

- **Find and access data from Microsoft Planetary Computer** *Use `pystac_client` to navigate STAC-oriented data and `stackstac` to read data as xarray objects*
- **Compare two similar datasets and evaluate differences, suitability for certain use cases** *read in data as xarray objects, organize and perform comparison*
- **Time series analysis of SAR RTC imagery** *Use xarray tools such as grouping, resampling and reductions as well as rioxarray functionality to organize and analyze SAR backscatter time series data*


# Tutorial Outline

## Chapter 1: Data access and organization

[Chapter 1](ch1_root.md) focuses on accessing Radiometric Terrain Corrected Sentinel-1 imagery. It contains three notebooks that cover steps related to reading and organizing data as ready-to-use xarray data cubes with x,y and time dimensions and appropriate metadata. The first demonstrates accessing Sentinel-1 RTC imagery that has been processed by ASF and preparing it for analysis. The second shows preliminary inspection and exploration of the prepared ASF data. The third notebook contains an example of accessing and working with Sentinel-1 RTC imagery processed and hosted by Microsoft Planetary Computer. This notebook focuses on working with [STAC](https://stacspec.org/en) data and using python packages such as `pystac_client` and `stackstac` to access data from a cloud-hosted repository and format it as easy-to-work-with xarray objects.

## Chapter 2: Dataset comparison and preliminary analysis

[Chapter 2](ch2_root.md) makes use of the datasets prepared in chapter 1. The first notebook demonstrates a comparison of the RTC imagery processed by ASF and by Microsoft Planetary Computer. The second contains an example of preliminary time series analysis of backscatter variability over proglacial lakes in the Himalayas. 
