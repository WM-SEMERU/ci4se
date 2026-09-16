def poke_assoc(store, objname, assoc, container, visited=None, _stack=None):
    try:
        sub_container = store.newContainer(objname, assoc, container)
    except (SystemExit, KeyboardInterrupt):
        raise
    except:
        raise ValueError('generic poke not supported by store')
    escape_keys = assoc and not all(isinstance(iobjname, strtypes) for 
        iobjname, _ in assoc)
    reported_item_counter = 0
    escaped_key_counter = 0
    try:
        if escape_keys:
            store.setRecordAttr('key', 'escaped', sub_container)
            verbose = store.verbose
            for obj in assoc:
                store.poke(str(escaped_key_counter), obj, sub_container,
                    visited=visited, _stack=_stack)
                escaped_key_counter += 1
                if store.verbose:
                    reported_item_counter += 1
                    if reported_item_counter == 9:
                        store.verbose = False
                        print('...')
            store.verbose = verbose
        else:
            for iobjname, iobj in assoc:
                store.poke(iobjname, iobj, sub_container, visited=visited,
                    _stack=_stack)
    except TypeError as e:
        msg = 'wrong type for keys in associative list'
        if e.args[0].startswith(msg):
            raise
        else:
            raise TypeError('{}:\n\t{}'.format(msg, e.args[0]))