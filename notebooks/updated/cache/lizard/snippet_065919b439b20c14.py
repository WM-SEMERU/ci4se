def wrap_uda(hdfs_file, inputs, output, update_fn, init_fn=None, merge_fn=
    None, finalize_fn=None, serialize_fn=None, close_fn=None, name=None):
    func = ImpalaUDA(inputs, output, update_fn, init_fn, merge_fn,
        finalize_fn, serialize_fn=serialize_fn, name=name, lib_path=hdfs_file)
    return func