def uuid_to_username(uuid):
    uuid_data = getattr(uuid, 'bytes', None) or UUID(uuid).bytes
    b32coded = base64.b32encode(uuid_data)
    return 'u-' + b32coded.decode('ascii').replace('=', '').lower()