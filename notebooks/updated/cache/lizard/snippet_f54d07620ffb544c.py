def user_info(authserver_host=None, authserver_port=None):
    authserver = get_auth_server_name(authserver_host, authserver_port)
    return DXHTTPRequest(authserver + '/system/getUserInfo', {},
        prepend_srv=False)