def set_uri(self, uri, size, checksum, readable=True, writable=False,
    storage_class=None):
    self.uri = uri
    self.size = size
    self.checksum = checksum
    self.writable = writable
    self.readable = readable
    self.storage_class = current_app.config['FILES_REST_DEFAULT_STORAGE_CLASS'
        ] if storage_class is None else storage_class
    return self