def db_getHex(self, db_name, key):
    warnings.warn('deprecated', DeprecationWarning)
    return (yield from self.rpc_call('db_getHex', [db_name, key]))