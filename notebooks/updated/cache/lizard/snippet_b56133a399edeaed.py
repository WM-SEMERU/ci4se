def ipv4_lstrip_zeros(address):
    obj = address.strip().split('.')
    for x, y in enumerate(obj):
        obj[x] = y.split('/')[0].lstrip('0')
        if obj[x] in ['', None]:
            obj[x] = '0'
    return '.'.join(obj)