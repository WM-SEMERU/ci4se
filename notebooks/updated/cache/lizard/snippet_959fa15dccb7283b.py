def pool_stop(name, **kwargs):
    conn = __get_conn(**kwargs)
    try:
        pool = conn.storagePoolLookupByName(name)
        return not bool(pool.destroy())
    finally:
        conn.close()