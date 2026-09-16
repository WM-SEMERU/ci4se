def write_gtiff_file(f_name, n_rows, n_cols, data, geotransform, srs,
    nodata_value, gdal_type=GDT_Float32):
    UtilClass.mkdir(os.path.dirname(FileClass.get_file_fullpath(f_name)))
    driver = gdal_GetDriverByName(str('GTiff'))
    try:
        ds = driver.Create(f_name, n_cols, n_rows, 1, gdal_type)
    except Exception:
        print('Cannot create output file %s' % f_name)
        return
    ds.SetGeoTransform(geotransform)
    try:
        ds.SetProjection(srs.ExportToWkt())
    except (AttributeError or Exception):
        ds.SetProjection(srs)
    ds.GetRasterBand(1).SetNoDataValue(nodata_value)
    if isinstance(data, numpy.ndarray) and data.dtype in [numpy.dtype('int'
        ), numpy.dtype('float')]:
        data = numpy.where(numpy.isnan(data), nodata_value, data)
    ds.GetRasterBand(1).WriteArray(data)
    ds = None