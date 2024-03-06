# Sentinel-1 Radiometric Terrain Corrected (RTC) Imagery + Xarray Tutorial Jupyter Book 
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://e-marshall.github.io/sentinel1_rtc)
[![DOI](https://zenodo.org/badge/537588743.svg)](https://zenodo.org/doi/10.5281/zenodo.10681095)

Sentinel-1 is a synthetic aperture radar (SAR) sensor operated by ESA that collects imaging data in C-band (~ 5 cm). Because Sentinel-1 has a side-looking viewing geometry, the data must undergo transformations and corrections to remove the effects of distortions due to surface topography and various radiometric characteristics and enable analysis in traditional geocoded coordinates. This tutorial focuses on Sentinel-1 imagery that has already had the corrections (radiometric terrain correction, RTC) applied. SAR datasets can be very large and unwieldy, and the RTC step can be computationally intensive. We focus on two publicly available Sentinel-1 RTC datasets: 1) Microsoft Planetary Computer processed and hosted global Sentinel-1 RTC dataset for 2019-2021 stored as cloud-optimized GeoTIFFs (COGs), and 2) Alaska Satellite Facility (ASF) hosted raw Sentinel-1 Single Look Complex (SLC) and Ground Range Detected (GRD) images with on-demand cloud processing resources for RTC and other processing needs. Imagery processed by ASF is available as COGs, though in this tutorial, we demonstrate working with the dataset as locally downloaded GeoTIFFs.

The tutorial contains instructions to install a local computing environment and download the dataset of ASF-processed Sentinel-1 RTC images hosted on Zenodo. Alternatively, users can download and run the tutorial using their own credentials, which are free to obtain and use. The tutorial links to resources for obtaining individual credentials. 

This tutorial takes the form of a jupyter book demonstrating accessing and working with Sentinel-1 RTC imagery using xarray. The tutorial demonstrates accessing and working with two datasets of Sentinel-1 RTC imagery: 
1) A time series processed by Alaska Satellite Facility's On-Demand Processing Server and downloaded locally as GeoTIFFs and 
2) A dataset processed and made available as cloud-optimized GeoTIFFs by Microsoft Planetary Computer.

The tutorial contains jupyter notebooks related to data access, organizing and handling metadata, data inspection, comparing datasets, and exploratory analysis and visualization, all focusing on demonstrating xarray functionality for remote sensing data workflows. 

Please don't hesitate to reach out with questions or feedback on this material. You can [raise an issue](https://github.com/e-marshall/sentinel1_rtc/issues), [start a discussion](https://github.com/e-marshall/sentinel1_rtc/discussions), or contact me via email (listed in tutorial). Thanks for stopping by! 

