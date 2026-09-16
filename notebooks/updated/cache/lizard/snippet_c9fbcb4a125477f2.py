def list_domains(**kwargs):
    vms = []
    conn = __get_conn(**kwargs)
    for dom in _get_domain(conn, iterable=True):
        vms.append(dom.name())
    conn.close()
    return vms