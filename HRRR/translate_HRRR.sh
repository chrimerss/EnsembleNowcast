#!/bin/bash

## Get wind band 32/33 for U/V
gdal_translate -b 101 -r near hrrr.t12z.wrfsfcf00.grib2 hrrr.wind_vel_u.tif
gdal_translate -b 102 -r near hrrr.t12z.wrfsfcf00.grib2 hrrr.wind_vel_v.tif

## Get Precipitation field 63 in kg/(m^2 s) * 3600

gdal_translate -b 63 -r near hrrr.t12z.wrfsfcf00.grib2 hrrr.rainrate.tif

## Warp to ESPG:4326 and crop to the area of interest
gdalwarp -t_srs EPSG:4326 -te -95.995757 29.4849 -94.9016 30.372 -ts 800 649 -r bilinear hrrr.wind_vel_u.tif hrrr.wind_vel_u_warp.tif
gdalwarp -t_srs EPSG:4326 -te -95.995757 29.4849 -94.9016 30.372 -ts 800 649 -r bilinear hrrr.wind_vel_v.tif hrrr.wind_vel_v_warp.tif

gdalwarp -t_srs EPSG:4326 -te -95.995757 29.4849 -94.9016 30.372 -ts 800 649 -r bilinear hrrr.rainrate.tif hrrr.rainrate_warp.tif
