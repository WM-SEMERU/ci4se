def from_file(cls, fp, storage=None):
    if storage is None:
        storage = cls.DEFAULT_STORAGE
    return cls.from_storage(storage.load(fp))