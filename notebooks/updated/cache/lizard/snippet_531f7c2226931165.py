def aggregate(cls, pipeline=None, **kwargs):
    return list(cls.collection.aggregate(pipeline or [], **kwargs))