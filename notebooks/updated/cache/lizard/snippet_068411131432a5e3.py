def conditional_write(strm, fmt, value, *args, **kwargs):
    if value is not None:
        strm.write(fmt.format(value, *args, **kwargs))