def rows_sum_init(hdf5_file, path, out_lock, *numpy_args):
    global g_hdf5_file, g_path, g_out, g_out_lock
    g_hdf5_file, g_path, g_out_lock = hdf5_file, path, out_lock
    g_out = to_numpy_array(*numpy_args)