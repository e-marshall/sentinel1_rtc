# functions for working with sentinel1 rtc imagery from asf and planetary computer

def points2coords(pt_ls): #should be [xmin, ymin, xmax, ymax]
    
    coords_ls = [(pt_ls[0], pt_ls[1]), (pt_ls[0], pt_ls[3]),
                 (pt_ls[2], pt_ls[3]), (pt_ls[2], pt_ls[1]),
                 (pt_ls[0], pt_ls[1])]
    return coords_ls
    

def extract_tif_fnames(scene_path):
    ''' return a list of files associated with a single S1 scene'''
    scene_files_ls = os.listdir(dir_path_all + scene_path)
    
    scene_files_vv = [fname for fname in scene_files_ls if fname.endswith('_VH.tif')]
    scene_files_vh = [fname for fname in scene_files_ls if fname.endswith('_VV.tif')]
    scene_files_ls = [fname for fname in scene_files_ls if fname.endswith('_ls_map.tif')]
    
    return scene_files_vv, scene_files_vh, scene_files_ls

def preprocess_vv(da_orig):
    '''function that should return an xarray object with time dimension and associated metadata given a path to a single RTC scene, if its dualpol will have multiple bands, currently just as 2 data arrays but could merge.
    goal would be to apply this a list of directories for different RTC products, return cube along time dimension - I think? 
    - for concatenating, would need to check footprints and only take products with the same footprint, or subset them all to a common AOI? '''

    
    da = da_orig.copy()
    da = da.rename({'band_data':'vv'}).squeeze()
    
    vv_fn = da_orig.encoding['source'][113:]
    
    sensor = vv_fn[0:3]
    beam_mode = vv_fn[4:6]
    acq_date_raw = vv_fn[7:15] #need to parse further
    acq_date = datetime.strptime(acq_date_raw, '%Y%m%d')
    acq_time = vv_fn[15:22]
    pol_type = vv_fn[24:25] # dual pol ...
    primary_pol = vv_fn[25:26] # VV ...
    orbit_type = vv_fn[26:27] #Precise (P), Restituted (R), or Original Predicted (O)
    terrain_correction_pixel_spacing = vv_fn[27:32] #Terrain Correction Pixel Spacing
    rtc_alg = vv_fn[33:34] #Software Package Used: GAMMA (G)
    output = vv_fn[35] #  Gamma-0 (g) or Sigma-0 (s) Output
    output_type = vv_fn[36] #Power (p) or Decibel (d) or Amplitude (a) Output
    masked = vv_fn[37]  #Unmasked (u) or Water Masked (w)
    filtered = vv_fn[38]  # Not Filtered (n) or Filtered (f)
    area =  vv_fn[39]       # Entire Area (e) or Clipped Area (c)
    tbd =   vv_fn[40]   #Dead Reckoning (d) or DEM Matching (m)
    product_id  = vv_fn[42:46]  #Product ID
    
    attrs_dict = { 'sensor': sensor,
                    'beam_mode':beam_mode, 
                    'acquisition_date' : acq_date,
                    'acquisition_time': acq_time,
                    'polarisation_type': pol_type,
                    'primary_polarisation': primary_pol,
                    'orbit_type': orbit_type,
                    'terrain_correction_pixel_spacing' : terrain_correction_pixel_spacing,
                    'output_format': output,
                    'output_type': output_type,
                    'masked' : masked,
                    'filtered':filtered,
                    'area':area,
                    'product_id': product_id 
             }
                    
    #link the strings for each of the above variables to their full names (from README, commented above)
    #eg if output_type=g, should read 'gamma'
    #add these as attrs to xr obj, make into dict first? 
    # parse acq_date to datetime, add as dim and coordinate to xr obj
    #add other metadata vars as attributes to xr obj
    
    da.attrs = attrs_dict
    
    utm_zone = da.spatial_ref.attrs['crs_wkt'][17:29]
    epsg_code =da.spatial_ref.attrs['crs_wkt'][589:594]
    
    da.attrs['utm_zone'] = utm_zone
    da.attrs['epsg_code'] = f'EPSG:{epsg_code}'
    
    date = da.attrs['acquisition_date']
    
    da = da.assign_coords({'acq_date':date})
    da = da.expand_dims('acq_date')
    da = da.drop_duplicates(dim=['x','y'])
    
    #vec = gpd.read_file('https://github.com/e-marshall/s1_book/raw/main/data/hma_lakes_aoi.geojson')
    #print(vec.crs)
    #da_clip = da.rio.clip(vec.geometry, vec.crs, drop=True)
    #print(da_clip.crs)
    
    return da

def preprocess_vh(da_orig):
    '''function that should return an xarray object with time dimension and associated metadata given a path to a single RTC scene, if its dualpol will have multiple bands, currently just as 2 data arrays but could merge.
    goal would be to apply this a list of directories for different RTC products, return cube along time dimension - I think? 
    - for concatenating, would need to check footprints and only take products with the same footprint, or subset them all to a common AOI? '''

    
    da = da_orig.copy()
    da = da.rename({'band_data':'vh'}).squeeze()
   
    vv_fn = da_orig.encoding['source'][113:]
    
    sensor = vv_fn[0:3]
    beam_mode = vv_fn[4:6]
    acq_date_raw = vv_fn[7:15] #need to parse further
    acq_date = datetime.strptime(acq_date_raw, '%Y%m%d')
    acq_time = vv_fn[15:22]
    pol_type = vv_fn[24:25] # dual pol ...
    primary_pol = vv_fn[25:26] # VV ...
    orbit_type = vv_fn[26:27] #Precise (P), Restituted (R), or Original Predicted (O)
    terrain_correction_pixel_spacing = vv_fn[27:32] #Terrain Correction Pixel Spacing
    rtc_alg = vv_fn[33:34] #Software Package Used: GAMMA (G)
    output = vv_fn[35] #  Gamma-0 (g) or Sigma-0 (s) Output
    output_type = vv_fn[36] #Power (p) or Decibel (d) or Amplitude (a) Output
    masked = vv_fn[37]  #Unmasked (u) or Water Masked (w)
    filtered = vv_fn[38]  # Not Filtered (n) or Filtered (f)
    area =  vv_fn[39]       # Entire Area (e) or Clipped Area (c)
    tbd =   vv_fn[40]   #Dead Reckoning (d) or DEM Matching (m)
    product_id  = vv_fn[42:46]  #Product ID
    
    attrs_dict = { 'sensor': sensor,
                    'beam_mode':beam_mode, 
                    'acquisition_date' : acq_date,
                    'acquisition_time': acq_time,
                    'polarisation_type': pol_type,
                    'primary_polarisation': primary_pol,
                    'orbit_type': orbit_type,
                    'terrain_correction_pixel_spacing' : terrain_correction_pixel_spacing,
                    'output_format': output,
                    'output_type': output_type,
                    'masked' : masked,
                    'filtered':filtered,
                    'area':area,
                    'product_id': product_id 
             }
                    
    #link the strings for each of the above variables to their full names (from README, commented above)
    #eg if output_type=g, should read 'gamma'
    #add these as attrs to xr obj, make into dict first? 
    # parse acq_date to datetime, add as dim and coordinate to xr obj
    #add other metadata vars as attributes to xr obj
    
    da.attrs = attrs_dict
    
    utm_zone = da.spatial_ref.attrs['crs_wkt'][17:29]
    epsg_code =da.spatial_ref.attrs['crs_wkt'][589:594]
    
    da.attrs['utm_zone'] = utm_zone
    da.attrs['epsg_code'] = f'EPSG:{epsg_code}'
    
    date = da.attrs['acquisition_date']
    
    da = da.assign_coords({'acq_date':date})
    da = da.expand_dims('acq_date')
    da = da.drop_duplicates(dim=['x','y'])
    
    return da

def preprocess_ls(da_orig):
    '''function that should return an xarray object with time dimension and associated metadata given a path to a single RTC scene, if its dualpol will have multiple bands, currently just as 2 data arrays but could merge.
    goal would be to apply this a list of directories for different RTC products, return cube along time dimension - I think? 
    - for concatenating, would need to check footprints and only take products with the same footprint, or subset them all to a common AOI? '''

    
    da = da_orig.copy()
    da = da.rename({'band_data':'layover_shadow_mask'}).squeeze()
    
    vv_fn = da_orig.encoding['source'][113:]
    
    sensor = vv_fn[0:3]
    beam_mode = vv_fn[4:6]
    acq_date_raw = vv_fn[7:15] #need to parse further
    acq_date = datetime.strptime(acq_date_raw, '%Y%m%d')
    acq_time = vv_fn[15:22]
    pol_type = vv_fn[24:25] # dual pol ...
    primary_pol = vv_fn[25:26] # VV ...
    orbit_type = vv_fn[26:27] #Precise (P), Restituted (R), or Original Predicted (O)
    terrain_correction_pixel_spacing = vv_fn[27:32] #Terrain Correction Pixel Spacing
    rtc_alg = vv_fn[33:34] #Software Package Used: GAMMA (G)
    output = vv_fn[35] #  Gamma-0 (g) or Sigma-0 (s) Output
    output_type = vv_fn[36] #Power (p) or Decibel (d) or Amplitude (a) Output
    masked = vv_fn[37]  #Unmasked (u) or Water Masked (w)
    filtered = vv_fn[38]  # Not Filtered (n) or Filtered (f)
    area =  vv_fn[39]       # Entire Area (e) or Clipped Area (c)
    tbd =   vv_fn[40]   #Dead Reckoning (d) or DEM Matching (m)
    product_id  = vv_fn[42:46]  #Product ID
    
    attrs_dict = { 'sensor': sensor,
                    'beam_mode':beam_mode, 
                    'acquisition_date' : acq_date,
                    'acquisition_time': acq_time,
                    'polarisation_type': pol_type,
                    'primary_polarisation': primary_pol,
                    'orbit_type': orbit_type,
                    'terrain_correction_pixel_spacing' : terrain_correction_pixel_spacing,
                    'output_format': output,
                    'output_type': output_type,
                    'masked' : masked,
                    'filtered':filtered,
                    'area':area,
                    'product_id': product_id 
             }
                    
    #link the strings for each of the above variables to their full names (from README, commented above)
    #eg if output_type=g, should read 'gamma'
    #add these as attrs to xr obj, make into dict first? 
    # parse acq_date to datetime, add as dim and coordinate to xr obj
    #add other metadata vars as attributes to xr obj
    
    da.attrs = attrs_dict
    
    utm_zone = da.spatial_ref.attrs['crs_wkt'][17:29]
    epsg_code =da.spatial_ref.attrs['crs_wkt'][589:594]
    
    da.attrs['utm_zone'] = utm_zone
    da.attrs['epsg_code'] = f'EPSG:{epsg_code}'
    
    date = da.attrs['acquisition_date']
    
    da = da.assign_coords({'acq_date':date})
    da = da.expand_dims('acq_date')
    da = da.drop_duplicates(dim=['x','y'])
    
    #vec = gpd.read_file('https://github.com/e-marshall/s1_book/raw/main/data/hma_lakes_aoi.geojson')
    #print(vec.crs)
    #da_clip = da.rio.clip(vec.geometry, vec.crs, drop=True)
    #print(da_clip.crs)
    
    return da

def power_to_db(input_arr):
    return (10*np.log10(np.abs(input_arr)))


def plot_timestep(input_arr, time_step_int):
    
    fig, axs = plt.subplots(ncols=3, figsize=(18,7))

    input_arr.isel(acq_date=time_step_int).ls.plot(ax=axs[0]);
    power_to_db(input_arr.isel(acq_date=time_step_int).vv).plot(ax=axs[1], cmap = plt.cm.Greys_r);
    power_to_db(input_arr.isel(acq_date=time_step_int).vh).plot(ax=axs[2], cmap = plt.cm.Greys_r);

    fig.suptitle(f'Layover-shadow mask (L), VV (C) and VH (R) backscatter {str(asf_clip.isel(acq_date=time_step_int).acq_date)[:-19]}')
    
def get_bbox_single(input_xr, buffer = 0):
    
    '''Takes input xr object (from itslive data cube), plots a quick map of the footprint. 
    currently only working for granules in crs epsg 32645'''

    xmin = input_xr.coords['x'].data.min()
    xmax = input_xr.coords['x'].data.max()

    ymin = input_xr.coords['y'].data.min()
    ymax = input_xr.coords['y'].data.max()

    pts_ls = [(xmin, ymin), (xmax, ymin),(xmax, ymax), (xmin, ymax), (xmin, ymin)]
 
    crs = input_xr.rio.crs

    polygon_geom = Polygon(pts_ls)
    polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom]) 
    polygon_prj = polygon
    polygon = polygon_prj.to_crs(crs)

    #add a buffer if needed
    bounds = polygon.total_bounds
    #bounds = [bounds[0]-500, bounds[2]+500, bounds[1]-500, bounds[3]+500]
    
    bounds_xmin = bounds[0]-buffer
    bounds_xmax = bounds[2]+buffer
    bounds_ymin = bounds[1]-buffer
    bounds_ymax = bounds[3]+buffer
    
    bounds_ls = [(bounds_xmin, bounds_ymin), (bounds_xmax, bounds_ymin),
                 (bounds_xmax, bounds_ymax), (bounds_xmin, bounds_ymax),
                 (bounds_xmin, bounds_ymin)]
                   
    
    bounds_geom = Polygon(bounds_ls)
    bound_gdf = gpd.GeoDataFrame(index=[0], crs=crs, geometry = [bounds_geom])
    bounds_prj = bound_gdf.to_crs(crs)
    
    return bounds_prj