def create_string_buffer(init, size=None, encoding=sys.getdefaultencoding()):
    if isinstance(init, six.string_types + (six.binary_type,)):
        if size is None:
            size = len(init) + 1
        buftype = c_char * size
        buf = buftype()
        try:
            buf.value = init.encode(encoding)
        except AttributeError:
            buf.value = init
        return buf
    elif isinstance(init, six.integer_types):
        buftype = c_char * init
        buf = buftype()
        return buf
    raise TypeError(init)