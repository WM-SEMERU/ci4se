def _rd_dat_file(file_name, dir_name, pb_dir, fmt, start_byte, n_samp):
    if fmt == '212':
        byte_count = _required_byte_num('read', '212', n_samp)
        element_count = byte_count
    elif fmt in ['310', '311']:
        byte_count = _required_byte_num('read', fmt, n_samp)
        element_count = byte_count
    else:
        element_count = n_samp
        byte_count = n_samp * BYTES_PER_SAMPLE[fmt]
    if pb_dir is None:
        with open(os.path.join(dir_name, file_name), 'rb') as fp:
            fp.seek(start_byte)
            sig_data = np.fromfile(fp, dtype=np.dtype(DATA_LOAD_TYPES[fmt]),
                count=element_count)
    else:
        sig_data = download._stream_dat(file_name, pb_dir, byte_count,
            start_byte, np.dtype(DATA_LOAD_TYPES[fmt]))
    return sig_data