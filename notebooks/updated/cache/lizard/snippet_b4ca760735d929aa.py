def get(cls, filter=None, **kwargs):
    document = cls(cls.find_one(filter, **kwargs))
    return document if document.document else None