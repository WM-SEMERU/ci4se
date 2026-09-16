def __patch_pipe_write_method(tango_device_klass, pipe):
    write_method = getattr(pipe, 'fset', None)
    if write_method:
        method_name = '__write_{0}__'.format(pipe.pipe_name)
        pipe.write_method_name = method_name
    else:
        method_name = pipe.write_method_name
        write_method = getattr(tango_device_klass, method_name)
    write_pipe = _get_wrapped_pipe_write_method(pipe, write_method)
    setattr(tango_device_klass, method_name, write_pipe)