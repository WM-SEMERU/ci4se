def dem(bounds, src_crs, dst_crs, out_file, resolution):
    if not dst_crs:
        dst_crs = 'EPSG:3005'
    bcdata.get_dem(bounds, out_file=out_file, src_crs=src_crs, dst_crs=
        dst_crs, resolution=resolution)