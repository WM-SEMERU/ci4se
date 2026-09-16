def zmq_send_data(socket, data, flags=0, copy=True, track=False):
    header, payload = [], []
    for key in sorted(data.keys()):
        arr = data[key]
        if not isinstance(arr, np.ndarray):
            raise DataError('Only ndarray types can be serialized')
        header.append(dict(dtype=str(arr.dtype), shape=arr.shape, key=key,
            aligned=arr.flags['ALIGNED']))
        payload.append(arr)
    msg = [json.dumps(header).encode('ascii')]
    msg.extend(payload)
    return socket.send_multipart(msg, flags, copy=copy, track=track)