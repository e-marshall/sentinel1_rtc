# Data cleaning and organization

The first chapter of this tutorial will demonstrate reading in and organizing Sentinel-1 RTC imagery processed by and accessed from two different sources.

## Data processed and downloaded from Alaska Satellite Facility

The first [notebook](asf_local_vrt.ipynb) (GDAL VRT approach) demonstrates working with data that was processed by Alaska Satellite Facility through their [Hyp3 On-Demand service](https://hyp3-docs.asf.alaska.edu/v2-transition/). The processed data is then downloaded locally. This notebook shows one approach for working with that data once downloaded locally.

The second [notebook](asf_inspect.ipynb) (ASF-processed RTC data inspection) shows preliminary dataset inspection of the ASF dataset once it has been read in and organized.

## Data processed and accessed from Microsoft Planetary Computer

This [notebook](PC_RTC.ipynb) (Microsoft Planetary Computer Sentinel-1 RTC Imagery) demonstrates accessing data from Microsoft Planetary Computer's catalog. Microsoft Planetary Computer performs RTC processing of Sentinel-1 imagery similarly to ASF. It is then made available as cloud-optimized GeoTIFFs and hosted on Microsoft Planetary Computer. This notebook demonstrates using STAC tools such as `pystac` and `stackstac` to access the cloud-hosted data locally. Microsoft Planetary Computer also hosts a jupyter hub server, which you could use instead of working with the data locally. Microsoft Planetary Computer requires a subscription (which is currently free). You can find out more about getting access [here](https://planetarycomputer.developer.azure-api.net/).
