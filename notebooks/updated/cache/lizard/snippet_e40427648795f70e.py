def find_one(cls, filter=None, *args, **kwargs):
    return cls.collection.find_one(filter, *args, **kwargs)