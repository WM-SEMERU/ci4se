def get(self, item):
    if isinstance(item, six.string_types):
        item = super(StorageClient, self).get(item)
    return item