# Introduction 

```{warning}
Thanks for coming to this site! Please note it is *under construction*. Content and code may not be in complete, working form at this time. Please reach out to emma.marshall@utah.edu with any comments/ questions about this work.
```

This tutorial will demonstrate various ways to access, process and work with Sentinel-1 Radiometrically Terrain Corrected imagery using the python package and open source project `xarray` as well as a number of other open source software packages. These examples are designed to show examples of data access, manipulation, processing and analysis workflows with complex datasets as well as to demonstrate common functionality of working with multi-dimensional gridded data using `xarray`. 

# Overview

This tutorial contains a number of jupyter notebooks that focus on working with Sentinel-1 imagery that has already undergone **Radiometric Terrain Correction (RTC)**. Because SAR imagery is collected from a side-looking sensor, it can contain distortions related to the viewing geometry of the sensor and the surface topography of the area being imaged. 

SAR data is collected in **slant range**, which is the viewing geometry of the side-looking sensor and has two dimensions: range and azimuth. These are the along-track and across-track directions of the imaged swath. As data is transformed from radar coordinates (slant range) to geocoded coordinates, the spaces that are represented by individual pixels in the two coordinate systems do not always align and distortions can arise due to certain viewing angle geometries and surface topography features. In addition, radiometric distortion can arise due to scattering responses from multiple scattering features within a single pixel. Radiometric terrain correction is a processing step that accounts for these distortions and the transformation from radar to geocoded coordinates that prepares SAR data for analysis. For a much more detailed explanation of this check out the Alaska Satellite Facility (ASF) [product guide for RTC imagery](https://hyp3-docs.asf.alaska.edu/guides/rtc_product_guide/). Chapter 2 of the [SAR Handbook](https://gis1.servirglobal.net/TrainingMaterials/SAR/Chp2Content.pdf) also has very useful descriptions of these concepts. 

There are multiple algorithms that perform radiometric terrain correction and it is important to understand the components of whichever dataset you use as well as their relative benefits and tradeoffs. This book will demonstrate accessing and working with two different (but similar) datasets of Sentinel-1 imagery that has undergone **Radiometric Terrain Correction**. Processing of SAR imagery can be very computationally intensive, so we focus on datasets that leverage cloud-computing resources, including both cloud-processed and cloud-hosted data as well as data that is processed in the cloud and then downloaded locally. 
(should I include discussion of what goes into RTC processing here or enough to link to other resources?)


(take out this paragraph if keeping next section)
The first two notebooks will show two approaches to working with the Sentinel-1 RTC imagery that is processed by ASF and downloaded locally. These will cover steps related to reading in the data and organizing it as ready-to-use xarray data cubes with x,y and time dimensions and appropriate metadata. The fourth notebook focuses on a different dataset of Sentinel-1 RTC imagery that has been processed and is hosted by Microsoft Planetary Computer. This notebook will focus on working with [STAC](https://stacspec.org/en) data and using python packages such as `pystac_client` and `stackstac` to access data from a cloud-hosted repository and format it as easy-to-work-with xarray objects. The fifth notebook will briefly compare the two RTC imagery datasets and demonstrate a number of xarray functions that are useful for these kinds of tasks and the sixth notebook will carry out a preliminary time series analysis of RTC imagery to show real-world applications of these datasets. 

# Tutorial Outline

## Chapter 1: Data access and organization

[Chapter 1](ch1_root.md) focuses on accessing Radiometric Terrain Corrected Sentinel-1 imagery. It contains two notebooks. The first demonstrates accessing Sentinel-1 RTC imagery that has been processed by ASF and preparing it for analysis. The second contains an example of accessing and working with Sentinel-1 RTC imagery processed and hosted by Microsoft Planetary Computer. 

## Chapter 2: Dataset comparison and preliminary analysis

[Chapter 2](ch2_root.md) makes use of the datasets prepared in chapter 1. The first notebook demonstrates comparing the RTC imagery processed by ASF and by Microsoft Planetary Computer. The second contains an example of preliminary time series analysis of backscatter variability over proglacial lakes in the Himalaya. 

# Learning objectives

This tutorial demonstrates accessing and working with different Sentinel-1 SAR RTC datasets. The learning goals include **domain specific steps related to working with synthetic aperture radar data** as well as specific *python and xarray techniques*. 

- **find and access data from Microsoft Planetary Computer** *Use `pystac_client` to navigate STAC-oriented data (wording) and `stackstac` to read data as xarray objects*
- **programmatically submit RTC processing jobs to be executed by Alaska Satellite Facility On-Demand Processing server using the HyP3 SDK package** *Organize, query and access processed data on your local machine*
- **compare two similar datasets and evaluate differences, suitability for certain use cases** *read in data as xarray objects, organize and perform comparison*
- **time series analysis of SAR RTC imagery** *Use xarray tools such as grouping, resampling and reductions as well as rioxarray functionality to organize and analyze SAR backscatter time series data*
