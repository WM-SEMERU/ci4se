def reduce_data_frame_evenly_with_gaps(df, valcol, target_len, maxgap, **kwargs
    ):
    return reduce_data_frame(df, slice_evenly_with_gaps(df[valcol],
        target_len, maxgap), **kwargs)