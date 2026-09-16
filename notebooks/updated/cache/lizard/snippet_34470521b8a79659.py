def hash_file(f):
    md5 = hashlib.md5()
    with open_filelike(f, 'rb') as f_obj:
        for chunk in iter(lambda : f_obj.read(128 * md5.block_size), b''):
            md5.update(chunk)
    return {'algorithm': 'md5', 'checksum': md5.hexdigest()}