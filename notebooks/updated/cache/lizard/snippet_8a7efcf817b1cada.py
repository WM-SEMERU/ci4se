def near(cls, collection, latitude, longitude, index_id, distance=None,
    skip=None, limit=None):
    kwargs = {'geo': index_id, 'latitude': latitude, 'longitude': longitude,
        'distance': distance, 'skip': skip, 'limit': limit}
    return cls._construct_query(name='near', collection=collection,
        multiple=True, **kwargs)