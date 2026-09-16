def servicegroup_server_up(sg_name, s_name, s_port, **connection_args):
    server = _servicegroup_get_server(sg_name, s_name, s_port, **
        connection_args)
    return server is not None and server.get_svrstate() == 'UP'