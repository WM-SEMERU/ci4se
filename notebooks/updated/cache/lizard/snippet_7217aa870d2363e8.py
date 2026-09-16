def _get_ann(dbs, features):
    value = ''
    for db, feature in zip(dbs, features):
        value += db + ':' + feature
    return value