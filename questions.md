# Dataset questions

Place to keep track of questions I've encountered while working with the ASF and PC RTC datasets...

1. ASF source granules are SLC images and PC are RTC, what effect does this have on the RTC product?

2. PC dataset doesn't appear to have a layover-shadow map?
3. ASF data has a layover shadow map, and some pixels masked out of the backscatter images, but it looks like there are layover pixels that aren't masked out in the data products. I thought you couldn't extract reliable data from pixels w/ layover?
4. product IDs / source files 
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

Two different groups within the ASF dataset? 

# Programming questions
1. feel like i'm relying on list comprehension a lot for creating, organizing objects - is there a more direct way to do these tasks? 
2. selecting off non-dimensional coordinates - keep messing up
3. dimensions of the ASF, PC objects are a bit of a mess, need to clean up