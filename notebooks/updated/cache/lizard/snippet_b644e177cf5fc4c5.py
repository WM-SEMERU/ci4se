def get(self, blob_hash):
    if blob_hash is None:
        return None
    store = blob_hash[STORE_HASH_LENGTH:]
    store = 'external' + ('-' if store else '') + store
    cache_folder = config.get('cache', None)
    blob = None
    if cache_folder:
        try:
            with open(os.path.join(cache_folder, blob_hash), 'rb') as f:
                blob = f.read()
        except FileNotFoundError:
            pass
    if blob is None:
        spec = self._get_store_spec(store)
        if spec['protocol'] == 'file':
            full_path = os.path.join(spec['location'], self.database, blob_hash
                )
            try:
                with open(full_path, 'rb') as f:
                    blob = f.read()
            except FileNotFoundError:
                raise DataJointError('Lost access to external blob %s.' %
                    full_path) from None
        elif spec['protocol'] == 's3':
            try:
                blob = S3Folder(database=self.database, **spec).get(blob_hash)
            except TypeError:
                raise DataJointError(
                    'External store {store} configuration is incomplete.'.
                    format(store=store))
        else:
            raise DataJointError('Unknown external storage protocol "%s"' %
                spec['protocol'])
        if cache_folder:
            if not os.path.exists(cache_folder):
                os.makedirs(cache_folder)
            safe_write(os.path.join(cache_folder, blob_hash), blob)
    return unpack(blob)