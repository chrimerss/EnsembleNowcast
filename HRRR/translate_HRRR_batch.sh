#!/bin/bash

files="/home/allen/Documents/Projects/Ensemble_Nowcast/HRRR/*.grib2"

for fname in $files
do
	base_name=$(basename $fname)
	## Get wind band 32/33 for U/V
	gdal_translate -b 32 -r near $fname "$base_name.wind_h.tif"
	gdal_translate -b 33 -r near $fname "$base_name.wind_v.tif"

	## Get Precipitation field 63 in kg/(m^2 s) * 3600

	gdal_translate -b 63 -r near $fname "$base_name.rainrate.tif"

	## Warp to ESPG:4326 and crop to the area of interest -96.334 28.289 -93.867 31.371 
	gdalwarp -t_srs EPSG:4326 -te -96.334 28.289 -93.867 31.371  -ts 247 308 -r bilinear "$base_name.wind_h.tif" "$base_name.wind_h_warp.tif"
	gdalwarp -t_srs EPSG:4326 -te -96.334 28.289 -93.867 31.371  -ts 247 308 -r bilinear "$base_name.wind_v.tif" "$base_name.wind_v_warp.tif"

	gdalwarp -t_srs EPSG:4326 -te -96.334 28.289 -93.867 31.371  -ts 247 308 -r near "$base_name.rainrate.tif" "$base_name.rainrate_warp.tif"

done

