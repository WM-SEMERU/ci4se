def connect(self, database, timezone=None, cache_size=0, auto_ensure=True,
    replica_set=None, *args, **kwds):
    safe = kwds.get('safe', False)
    if 'safe' in kwds:
        del kwds['safe']
    if timezone is not None:
        kwds['tz_aware'] = True
    if replica_set is not None:
        if 'MongoReplicaSetClient' in globals():
            conn = MongoReplicaSetClient(*args, replicaSet=replica_set, **kwds)
        else:
            conn = MongoClient(*args, replicaSet=replica_set, **kwds)
    else:
        conn = MongoClient(*args, **kwds)
    db = conn[database]
    return Session(db, timezone=timezone, safe=safe, cache_size=cache_size,
        auto_ensure=auto_ensure)