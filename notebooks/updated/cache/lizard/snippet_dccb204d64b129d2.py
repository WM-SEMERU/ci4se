def list_pools(**kwargs):
    conn = __get_conn(**kwargs)
    try:
        return [pool.name() for pool in conn.listAllStoragePools()]
    finally:
        conn.close()