def get_hash(file_path, checksum='sha1'):
    sha = getattr(hashlib, checksum)()
    with open(file_path) as file_descriptor:
        while True:
            chunk = file_descriptor.read(65536)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()