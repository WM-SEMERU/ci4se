def decode_base64_dict(data):
    b64 = base64.b64decode(data['__ndarray__'])
    array = np.copy(np.frombuffer(b64, dtype=data['dtype']))
    if len(data['shape']) > 1:
        array = array.reshape(data['shape'])
    return array