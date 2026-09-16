def setup(config, minconn=5, maxconn=10, adapter='mysql', key='default',
    slave=False):
    global __db
    if '.' in key:
        raise TypeError('The DB Key: "%s" Can\'t Contain dot' % key)
    if slave == False and key in __db:
        raise DBError('The Key: "%s" was set' % key)
    database = DB(config, minconn, maxconn, key, adapter)
    master_key = key
    slave_key = key + '.slave'
    if not slave:
        __db[master_key] = database
        if slave_key not in __db:
            __db[slave_key] = [database]
    elif key in __db:
        databases = __db[slave_key]
        if len(databases) == 1 and __db[master_key] == databases[0]:
            __db[slave_key] = [database]
        else:
            __db[slave_key].append(database)
    else:
        __db[slave_key] = [database]