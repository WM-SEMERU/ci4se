def do_version():
    v = ApiPool.ping.model.Version(name=ApiPool().current_server_name,
        version=ApiPool().current_server_api.get_version(), container=
        get_container_version())
    log.info('/version: ' + pprint.pformat(v))
    return v