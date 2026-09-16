def hash_data(data, blocksize=65536):
    data = pickle.dumps(data)
    hasher = hashlib.sha1()
    hasher.update(data)
    return hasher.hexdigest()