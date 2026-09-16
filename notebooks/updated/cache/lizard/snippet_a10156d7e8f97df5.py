def file_path_from_hash(self, file_hash, path=None, hash_list=None):
    if hash_list is None:
        hash_list = list(file_hash)
    if not hash_list:
        raise IOError('Directory structure is too full!')
    if not path:
        path = os.path.join(self.path, hash_list.pop(0))
    files = os.listdir(path)
    if file_hash in files:
        full_path = os.path.join(path, file_hash)
        if os.path.isfile(full_path):
            return PathAndHash(path=full_path, hash=file_hash)
        return PathAndHash(path=full_path + '/', hash=file_hash)
    next_path = os.path.join(path, hash_list.pop(0))
    if not os.path.exists(next_path):
        raise IOError('File not found in the structure.')
    return self.file_path_from_hash(file_hash=file_hash, path=next_path,
        hash_list=hash_list)