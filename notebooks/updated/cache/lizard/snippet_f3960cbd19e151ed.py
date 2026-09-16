def get(no_create=False, server=None, port=None, force_uuid=None):
    pid = os.getpid()
    thread = threading.current_thread()
    wdb = Wdb._instances.get((pid, thread))
    if not wdb and not no_create:
        wdb = object.__new__(Wdb)
        Wdb.__init__(wdb, server, port, force_uuid)
        wdb.pid = pid
        wdb.thread = thread
        Wdb._instances[pid, thread] = wdb
    elif wdb:
        if (server is not None and wdb.server != server or port is not None and
            wdb.port != port):
            log.warn('Different server/port set, ignoring')
        else:
            wdb.reconnect_if_needed()
    return wdb