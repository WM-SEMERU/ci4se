def get_connection(cls, pid, connection):
    with cls._lock:
        return cls._pools[pid].connection_handle(connection)