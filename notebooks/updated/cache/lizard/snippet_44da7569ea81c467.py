def atlas_peer_table_lock():
    global PEER_TABLE_LOCK, PEER_TABLE, PEER_TABLE_LOCK_HOLDER, PEER_TABLE_LOCK_TRACEBACK
    if PEER_TABLE_LOCK_HOLDER is not None:
        assert PEER_TABLE_LOCK_HOLDER != threading.current_thread(), 'DEADLOCK'
    PEER_TABLE_LOCK.acquire()
    PEER_TABLE_LOCK_HOLDER = threading.current_thread()
    PEER_TABLE_LOCK_TRACEBACK = traceback.format_stack()
    return PEER_TABLE