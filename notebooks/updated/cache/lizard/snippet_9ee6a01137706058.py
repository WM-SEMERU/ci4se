def stop(name, call=None):
    conn = get_conn()
    node = get_node(conn, name)
    log.debug('Node of Cloud VM: %s', node)
    status = conn.ex_shutdown_graceful(node)
    log.debug('Status of Cloud VM: %s', status)
    return status