def convert_catalog_id_to_object_id_string(catalog_id):
    if not isinstance(catalog_id, Id):
        raise TypeError('input needs to be an Id')
    seed_str = catalog_id.get_identifier() + catalog_id.get_authority(
        ) + '000000000000'
    try:
        seed_str = str.encode(seed_str[:12])
    except TypeError:
        seed_str = seed_str[:12]
    seed_str = binascii.hexlify(seed_str)
    try:
        seed_str = str(seed_str, 'utf8')
    except TypeError:
        seed_str = str(seed_str)
    return seed_str