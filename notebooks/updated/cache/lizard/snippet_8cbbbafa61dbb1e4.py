def parse_data_df(data_dset, ridx, cidx, row_meta, col_meta):
    if len(ridx) == len(row_meta.index) and len(cidx) == len(col_meta.index):
        data_array = np.empty(data_dset.shape, dtype=np.float32)
        data_dset.read_direct(data_array)
        data_array = data_array.transpose()
    elif len(ridx) <= len(cidx):
        first_subset = data_dset[:, (ridx)].astype(np.float32)
        data_array = first_subset[(cidx), :].transpose()
    elif len(cidx) < len(ridx):
        first_subset = data_dset[(cidx), :].astype(np.float32)
        data_array = first_subset[:, (ridx)].transpose()
    data_df = pd.DataFrame(data_array, index=row_meta.index[ridx], columns=
        col_meta.index[cidx])
    return data_df