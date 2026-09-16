def get_all_keys(reactor, key_type, value_type, etcd_address):
    etcd = Client(reactor, etcd_address)
    result = yield etcd.get(b'\x00', range_end=b'\x00')
    res = {}
    for item in result.kvs:
        if key_type == 'utf8':
            key = item.key.decode('utf8')
        elif key_type == 'binary':
            key = binascii.b2a_base64(item.key).decode().strip()
        else:
            raise Exception('logic error')
        if value_type == 'json':
            value = json.loads(item.value.decode('utf8'))
        elif value_type == 'binary':
            value = binascii.b2a_base64(item.value).decode().strip()
        elif value_type == 'utf8':
            value = item.value.decode('utf8')
        else:
            raise Exception('logic error')
        res[key] = value
    returnValue(res)