def unpack_variable(var):
    if var.dataType == stream.STRUCTURE:
        return None, struct_to_dtype(var), 'Structure'
    elif var.dataType == stream.SEQUENCE:
        log.warning('Sequence support not implemented!')
    dt = data_type_to_numpy(var.dataType, var.unsigned)
    if var.dataType == stream.OPAQUE:
        type_name = 'opaque'
    elif var.dataType == stream.STRING:
        type_name = 'string'
    else:
        type_name = dt.name
    if var.data:
        log.debug('Storing variable data: %s %s', dt, var.data)
        if var.dataType == stream.STRING:
            data = var.data
        else:
            data = np.frombuffer(var.data, dtype=dt.newbyteorder('>'))
    else:
        data = None
    return data, dt, type_name