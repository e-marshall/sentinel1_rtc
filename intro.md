# Thanks for coming to this site! Please note it is *under construction*
Content and code may not be in complete, working form at this time. Please reach out to emma.marshall@utah.edu with any comments/ questions about this work.

# Introduction 

This tutorial will demonstrate various ways to access, process and work with Sentinel-1 Radiometrically Terrain Corrected imagery using the python package and open source project `xarray` as well as a number of other open source software packages. These examples are designed to show examples of data access, manipulation, processing and analysis workflows with complex datasets as well as to demonstrate common functionality of working with multi-dimensional gridded data using `xarray`. 

# Overview

This tutorial contains a number of jupyter notebooks that focus on working with Sentinel-1 imagery that has had Radiometric Terrain Correction (RTC) applied to it. Because SAR imagery is collected from a side-looking sensor, it can contain distortions related to the viewing geometry of the sensor and the surface topography of the area being imaged. 


SAR data is collected in **slant rang**, which is the viewing geometry of the side-looking sensor and has two dimensions: range and azimuth. These are the along-track and across-track directions of the imaged swath. For a much more detailed explanation of this check out this [page](). To use SAR data to examine Earth's surface, we need to **geocode** it into x and y coordinates. As data is transformed from radar coordinates to geocoded coordinates, the spaces that are represented by individual pixels in the two coordinate systems do not always align. This is where we use a digital elevation model to remove some issues, but there are specific distortions related to radar viewing geometry and high-relief surface topography that need to be corrected as well. 

There are multiple algorithms that perform radiometric terrain correction and it is important to understand the components of whichever dataset you use as well as their relative benefits and tradeoffs. This book will demonstrate accessing and working with two different (but similar) datasets of Sentinel-1 imagery that has undergone **Radiometric Terrain Correction**. Processing of SAR imagery can be very computationally intensive, so we focus on datasets that leverage cloud-computing resources, including both cloud-processed and cloud-hosted data as well as data that is processed in the cloud and then downloaded locally. 

The first three notebooks will focus on Sentinel-1 RTC imagery that is processed by Alaska Satellite Facility (ASF). The first notebook will demonstrate how to submit processing jobs programmatically to ASF's On-Demand Processing Server. The following two notebooks will show two approaches to working with the ASF-processed data once it has been downloaded locally- these will cover steps related to reading in the data and organizing it as ready-to-use xarray data cubes with x,y and time dimensions. The fourth notebook focuses on a different dataset of Sentinel-1 RTC imagery that has been processed and is hosted by Microsoft Planetary Computer. This notebook will focus on working with [STAC]() data and using python packages such as `pystac_client` and `stackstac` to access data from a cloud-hosting repository and format it as easy-to-work-with xarray objects. The fifth notebook will briefly compare the two RTC imagery datasets and demonstrate a number of xarray functions that are useful for these kinds of tasks and the sixth notebook will carry out a preliminary time series analysis of RTC imagery to show real-world applications of these datasets. 

# Learning objectives

This tutorial demonstrates accessing and working with different Sentinel-1 SAR RTC datasets. The learning goals include **domain specific steps related to working with synthetic aperture radar data** as well as specific *python and xarray techniques*. 

- **find and access data from Microsoft Planetary Computer** *Use `pystac_client` to navigate STAC-oriented data (wording) and `stackstac` to read data as xarray objects*
- **programmatically submit RTC processing jobs to be executed by Alaska Satellite Facility On-Demand Processing server using the HyP3 SDK package** *Organize, query and access processed data on your local machine*
- **compare two similar datasets and evaluate differences, suitability for certain use cases** *read in data as xarray objects, organize and perform comparison*
- **time series analysis of SAR RTC imagery** *Use xarray tools such as grouping, resampling and reductions as well as rioxarray functionality to organize and analyze SAR backscatter time series data*

# Tutorial Structure

1. ASF RTC data
    a. submitting HyP3 jobs <br>
    b. working with processed data: `open_mfdataset()` <br>
    c. workign with processed data: `VRT` <br>
2. Planetary Computer RTC data
3. Dataset comparison
4. time series analysis. 

