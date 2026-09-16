def show_disk(name=None, kwargs=None, call=None):
    if not kwargs or 'disk_name' not in kwargs:
        log.error('Must specify disk_name.')
        return False
    conn = get_conn()
    return _expand_disk(conn.ex_get_volume(kwargs['disk_name']))