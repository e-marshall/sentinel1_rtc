# Tutorial structure questions 
a. intro
1. need more discussino of RTC processing?
b. asf data, xr.open_mfdataset()
~~1. helpful to include image of directory structure for local files?
~2. worth describing the area of interest/why it was chosen more in clipping by vector section? -- or maybe elsewhere in tutorial, but worht including more introduction on area?
c. PC data access
1. worth mentioning differences btw VV, VH returns/ linking to SAR handbook explanation of polarization? not sure right balance between 'science-y' and demonstrating workflow/code
d. dataset comparison
e. time series example
1. maybe take this out? feel like its getting long..

# Dataset questions

Place to keep track of questions I've encountered while working with the ASF and PC RTC datasets...

1. ASF source granules are SLC images and PC are RTC, what effect does this have on the RTC product?

2. PC dataset doesn't appear to have a layover-shadow map?
~~4. product IDs / source files 
    - ASF provides a 4-digit product key in the filename, but it doesn't look like this directly corresponds to the source granule?
    eg. product ID = 1424 for RTC image from source granule: S1A_IW_SLC__1SDV_20210502T121414_20210502T121441_037709_047321_900F
    - can pull this from the README for that file - but is there a better way to do this?
    - PC includes product id as a coordinate variable: eg. 'S1A_IW_GRDH_1SDV_20210602T120544_20210602T120609_038161_0480FD_rtc'.
    - is there a better way to compare ASF, PC RTC images from the same S1 acquisitions than pulling the granule ID from the ASF product readme?
    - it doesn't look like PC provides a mapping back to source granule? 
    
## PC RTC imagery
- radiometric terrain correction performed on GRD images that have already been multilooked, ground-projected
- methods description [here](https://planetarycomputer.microsoft.com/dataset/sentinel-1-rtc)

## ASF RTC imagery
- because using SLC source imagery, terrain correction performed in slant range, then corrected image is mapped to DEM space
- geocoding is final step
- methods description [here](https://hyp3-docs.asf.alaska.edu/guides/rtc_product_guide/)

# Programming questions
1. feel like i'm relying on list comprehension a lot for creating, organizing objects - is there a more direct way to do these tasks? 
5. xarray open_mfdataset() -- can you specify input args in addition to the xr object? ie want to perform the same preprocessing to different variables stored in different tiff files (VV, VH, layover-shadow map). 
6. docs on assigning non-dimensional xr coords? 


ufunc
https://docs.xarray.dev/en/stable/examples/apply_ufunc_vectorize_1d.html
https://stackoverflow.com/questions/57419541/how-to-use-apply-ufunc-with-numpy-digitize-for-each-image-along-time-dimension-o/57513184#57513184
https://github.com/pydata/xarray/issues/2808
