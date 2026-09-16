def makeService(cls, options):
    from axiom.store import Store
    jm = options['journal-mode']
    if jm is not None:
        jm = jm.decode('ascii')
    store = Store(options['dbdir'], debug=options['debug'], journalMode=jm)
    service = IService(store)
    _CheckSystemVersion(store).setServiceParent(service)
    return service