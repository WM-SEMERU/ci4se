def parse(file_path, convert_neg_666=True, rid=None, cid=None, ridx=None,
    cidx=None, row_meta_only=False, col_meta_only=False, make_multiindex=False
    ):
    assert sum([row_meta_only, col_meta_only]
        ) <= 1, 'row_meta_only and col_meta_only cannot both be requested.'
    nan_values = ['#N/A', 'N/A', 'NA', '#NA', 'NULL', 'NaN', '-NaN', 'nan',
        '-nan', '#N/A!', 'na', 'NA', 'None', '#VALUE!']
    if convert_neg_666:
        nan_values.append('-666')
    if not os.path.exists(file_path):
        err_msg = (
            'The given path to the gct file cannot be found. gct_path: {}')
        logger.error(err_msg.format(file_path))
        raise Exception(err_msg.format(file_path))
    logger.info('Reading GCT: {}'.format(file_path))
    (version, num_data_rows, num_data_cols, num_row_metadata, num_col_metadata
        ) = read_version_and_dims(file_path)
    row_metadata, col_metadata, data = parse_into_3_df(file_path,
        num_data_rows, num_data_cols, num_row_metadata, num_col_metadata,
        nan_values)
    myGCToo = create_gctoo_obj(file_path, version, row_metadata,
        col_metadata, data, make_multiindex)
    if (rid is not None or ridx is not None or cid is not None or cidx is not
        None):
        logger.info(
            'Subsetting GCT... (note that there are no speed gains when subsetting GCTs)'
            )
        myGCToo = sg.subset_gctoo(myGCToo, rid=rid, cid=cid, ridx=ridx,
            cidx=cidx)
    if row_meta_only:
        return myGCToo.row_metadata_df
    elif col_meta_only:
        return myGCToo.col_metadata_df
    else:
        return myGCToo