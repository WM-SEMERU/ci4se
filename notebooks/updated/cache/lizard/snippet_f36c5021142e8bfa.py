def memwarp_multi_fn(src_fn_list, res='first', extent='intersection', t_srs
    ='first', r='cubic', verbose=True, dst_ndv=0):
    if not iolib.fn_list_check(src_fn_list):
        sys.exit('Missing input file(s)')
    src_ds_list = [gdal.Open(fn, gdal.GA_ReadOnly) for fn in src_fn_list]
    return memwarp_multi(src_ds_list, res, extent, t_srs, r, verbose=
        verbose, dst_ndv=dst_ndv)