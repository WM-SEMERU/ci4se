def write(gctoo_object, out_file_name, convert_back_to_neg_666=True,
    gzip_compression_level=6, max_chunk_kb=1024, matrix_dtype=numpy.float32):
    gctx_out_name = add_gctx_to_out_name(out_file_name)
    hdf5_out = h5py.File(gctx_out_name, 'w')
    write_version(hdf5_out)
    write_src(hdf5_out, gctoo_object, gctx_out_name)
    elem_per_kb = calculate_elem_per_kb(max_chunk_kb, matrix_dtype)
    chunk_size = set_data_matrix_chunk_size(gctoo_object.data_df.shape,
        max_chunk_kb, elem_per_kb)
    hdf5_out.create_dataset(data_matrix_node, data=gctoo_object.data_df.
        transpose().values, dtype=matrix_dtype)
    write_metadata(hdf5_out, 'col', gctoo_object.col_metadata_df,
        convert_back_to_neg_666, gzip_compression=gzip_compression_level)
    write_metadata(hdf5_out, 'row', gctoo_object.row_metadata_df,
        convert_back_to_neg_666, gzip_compression=gzip_compression_level)
    hdf5_out.close()