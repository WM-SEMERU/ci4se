def retrieve_blob(self, key, encoding=None):
    blob_key = self.__retrieve(key)
    if blob_key is None:
        return None
    if not blob_key:
        raise Exception('Invalid blob_key')
    elif blob_key == JiCache.INTERNAL_BLOB:
        blob_data = self.__retrieve_internal_blob(key)
        return blob_data if not encoding else blob_data.decode(encoding)
    else:
        getLogger().debug('Key[{key}] -> [{blob_key}]'.format(key=key,
            blob_key=blob_key))
        blob_file = os.path.join(self.blob_location, blob_key)
        return FileHelper.read(blob_file)