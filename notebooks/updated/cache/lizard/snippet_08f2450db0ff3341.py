def pokeStorable(self, storable, objname, obj, container, visited=None,
    _stack=None, **kwargs):
    storable.poke(self, objname, obj, container, visited=visited, _stack=
        _stack, **kwargs)
    try:
        record = self.getRecord(objname, container)
    except KeyError:
        if self.verbose:
            print('skipping `{}` (type: {})'.format(objname, storable.
                storable_type))
            if 1 < self.verbose:
                print(traceback.format_exc())
    else:
        self.setRecordAttr('type', storable.storable_type, record)
        if storable.version is not None:
            self.setRecordAttr('version', from_version(storable.version),
                record)