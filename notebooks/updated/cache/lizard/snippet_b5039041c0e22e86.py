def write_map(fo, datum, schema):
    if len(datum) > 0:
        write_long(fo, len(datum))
        vtype = schema['values']
        for key, val in iteritems(datum):
            write_utf8(fo, key)
            write_data(fo, val, vtype)
    write_long(fo, 0)