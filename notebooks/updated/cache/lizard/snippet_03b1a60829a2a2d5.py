def get_graphics(vm_, **kwargs):
    conn = __get_conn(**kwargs)
    graphics = _get_graphics(_get_domain(conn, vm_))
    conn.close()
    return graphics