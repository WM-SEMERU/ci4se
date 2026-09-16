def get_rows_to_keep(gctoo, rid=None, row_bool=None, ridx=None, exclude_rid
    =None):
    if rid is not None:
        assert type(rid) == list, 'rid must be a list. rid: {}'.format(rid)
        rows_to_keep = [gctoo_row for gctoo_row in gctoo.data_df.index if 
            gctoo_row in rid]
        num_missing_rids = len(rid) - len(rows_to_keep)
        if num_missing_rids != 0:
            logger.info('{} rids were not found in the GCT.'.format(
                num_missing_rids))
    elif row_bool is not None:
        assert len(row_bool) == gctoo.data_df.shape[0
            ], 'row_bool must have length equal to gctoo.data_df.shape[0]. ' + 'len(row_bool): {}, gctoo.data_df.shape[0]: {}'.format(
            len(row_bool), gctoo.data_df.shape[0])
        rows_to_keep = gctoo.data_df.index[row_bool].values
    elif ridx is not None:
        assert type(ridx[0]) is int, (
            'ridx must be a list of integers. ridx[0]: {}, ' +
            'type(ridx[0]): {}').format(ridx[0], type(ridx[0]))
        assert max(ridx) <= gctoo.data_df.shape[0], (
            'ridx contains an integer larger than the number of rows in ' +
            'the GCToo. max(ridx): {}, gctoo.data_df.shape[0]: {}').format(max
            (ridx), gctoo.data_df.shape[0])
        rows_to_keep = gctoo.data_df.index[ridx].values
    else:
        rows_to_keep = gctoo.data_df.index.values
    if exclude_rid is not None:
        rows_to_keep = [row_to_keep for row_to_keep in rows_to_keep if 
            row_to_keep not in exclude_rid]
    return rows_to_keep