def load(filename):
    file = open(filename, 'rb')
    container = std_pickle.load(file)
    file.close()
    db = Database(file.name)
    chains = 0
    funs = set()
    for k, v in six.iteritems(container):
        if k == '_state_':
            db._state_ = v
        else:
            db._traces[k] = Trace(name=k, value=v, db=db)
            setattr(db, k, db._traces[k])
            chains = max(chains, len(v))
            funs.add(k)
    db.chains = chains
    db.trace_names = chains * [list(funs)]
    return db