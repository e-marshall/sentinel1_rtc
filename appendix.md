# Appendix

## Things I tried that didn't work out (but might still be useful...)

### `xr.open_mfdataset()`

Xarray's `xr.open_mfdataset()` [function](https://docs.xarray.dev/en/stable/generated/xarray.open_mfdataset.html) allows the user to read in and combine multiple files at once to produce a single `xr.DataArray` object. I first used this to read in the geotiff files for each ASF-processed scene of Sentinel-1 RTC imagery. The `xr.open_mfdataset()` function takes a preprocess argument which allows you to write a function that specifies how each raster file is read in so that the structure and metadata of the returned object is correct. This gives you a lot of flexibility and makes reading in a large stack of files very smooth.

However, for this dataset, I found that the `xr.open_mfdataset()` function wasn't a great fit. The raster stack all covered a common area of interest, but each file did not have the exact same spatial footprint. This created problems when specifying a chunking strategy, because the chunking was defined off of the first file in the stack, but would not be appropriate for files further down in the stack with different borders. The processing would work fine for all lazy steps, but a memory 'blow-up' would occur when I tried to perform a step that required computation. I initially thought I had bypassed this issue by clipping the returned dataset to the spatial extent of my area of interest (much smaller), but soon realized that this process encountered memory issues as well. 

```{note}
The stack I used contains multiple scenes that cover the same area of interest (multiple viewing geometries). If you wanted to select only scenes from a single viewing geometry at the expense of a denser time series, `xr.open_mfdataset()` might work a bit better (I didn't try this so cannot say for sure)
```

Ultimately, I decided to use the approach of creating GDAL VRT objects, and reading those in with `rioxarray.open_rasterio()` to organize the data as xarray objects. This worked much better from a memory perspective but created much more work with organizing metadata and structuring the dataset in an analysis-ready format. The `xr.open_mfdataset()` function seems like a much more efficient approach if your dataset is well-aligned with its parameters (ie. a spatially uniform stack). While it did not end up being the best tool for this task, I decided to include the notebook with the `xr.open_mfdataset()` approach anyway, in case it is useful to see a demonstration of this function. I learned a lot about how to structure a `preprocess` function and many other steps working on this example. 

Take a look at the notebook using `xr.open_mfdataset()` to read in stacks of ASF-processed Sentinel-1 RTC imagery files [here](asf_local_mf.ipynb)

In addition to the documentation linked above, some other useful resources for `xr.open_mfdataset()` that I found are: 

- This stack overflow [answer](https://stackoverflow.com/questions/51709266/using-xarray-to-open-a-multi-file-dataset-when-both-the-files-and-dataset-have-a) contains an example of a preprocess function.
- This github [issue](https://github.com/pydata/xarray/issues/2550) talks about accessing filename from within the preprocess function <-- is there a better example to link to here? 