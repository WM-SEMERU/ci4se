def demux_adaptor(stream_id, data):
    if stream_id == STDOUT:
        return data, None
    elif stream_id == STDERR:
        return None, data
    else:
        raise ValueError('{0} is not a valid stream'.format(stream_id))