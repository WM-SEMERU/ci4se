def hydrate(cls, db, bucket, limit, key):
    return cls(db, limit, key, **bucket)