def sentinel_get_master_ip(master, host=None, port=None, password=None):
    server = _sconnect(host, port, password)
    ret = server.sentinel_get_master_addr_by_name(master)
    return dict(list(zip(('master_host', 'master_port'), ret)))