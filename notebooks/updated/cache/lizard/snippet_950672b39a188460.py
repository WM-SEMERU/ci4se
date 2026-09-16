def write_src(hdf5_out, gctoo_object, out_file_name):
    if gctoo_object.src == None:
        hdf5_out.attrs[src_attr] = out_file_name
    else:
        hdf5_out.attrs[src_attr] = gctoo_object.src