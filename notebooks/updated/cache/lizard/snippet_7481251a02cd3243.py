def get_column_metadata(gctx_file_path, convert_neg_666=True):
    full_path = os.path.expanduser(gctx_file_path)
    gctx_file = h5py.File(full_path, 'r')
    col_dset = gctx_file[col_meta_group_node]
    col_meta = parse_metadata_df('col', col_dset, convert_neg_666)
    gctx_file.close()
    return col_meta