def write(gctoo, out_fname, data_null='NaN', metadata_null='-666',
    filler_null='-666', data_float_format='%.4f'):
    if not out_fname.endswith('.gct'):
        out_fname += '.gct'
    f = open(out_fname, 'w')
    dims = [str(gctoo.data_df.shape[0]), str(gctoo.data_df.shape[1]), str(
        gctoo.row_metadata_df.shape[1]), str(gctoo.col_metadata_df.shape[1])]
    write_version_and_dims(VERSION, dims, f)
    write_top_half(f, gctoo.row_metadata_df, gctoo.col_metadata_df,
        metadata_null, filler_null)
    write_bottom_half(f, gctoo.row_metadata_df, gctoo.data_df, data_null,
        data_float_format, metadata_null)
    f.close()
    logger.info('GCT has been written to {}'.format(out_fname))