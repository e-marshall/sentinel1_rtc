# Data cleaning and organization

The first chapter of this tutorial will demonstrate reading in and organizing Sentinel-1 RTC imagery processed by and accessed from two different sources.

## Data processed and downloaded from Alaska Satellite Facility

This [notebook](asf_local_vrt.ipynb) demonstrates working with data that was processed by Alaska Satellite Facility through their On-Demand server using HyP-3 SDK to submit jobs programmatically. The processed data is then downloaded locally. This notebook shows one approach for working with that data once its been downloaded locally.

## Data processed and accessed from Microsoft Planetary Computer

This [notebook](PC_RTC.ipynb) demonstrates accessing data from Microsoft Planetary Computer's catalog. Microsoft Planetary Computer performs RTC processing of Sentinel-1 imagery similarly to ASF. It is then made available as cloud-optimized geotiffs and hosted on Microsoft Planetary Computer. This notebook demonstrates using STAC tools such as `pystac` and `stackstac` to access the cloud-hosted data locally. Microsoft Planetary Computer also hosts a jupyter hub server which you could access and use instead of doing so locally. Microsoft Planetary Computer requires a subscription (currently free). You can find out more about getting access [here](https://planetarycomputer.developer.azure-api.net/).
