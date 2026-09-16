def get_md5_hash(file_path):
    checksum = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda : f.read(128 * checksum.block_size), b''):
            checksum.update(chunk)
    return checksum.hexdigest()