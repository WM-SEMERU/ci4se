def get_xray_daemon():
    env_value = os.environ.get('AWS_XRAY_DAEMON_ADDRESS')
    if env_value is None:
        raise XRayDaemonNotFoundError()
    xray_ip, xray_port = env_value.split(':')
    return XRayDaemon(ip_address=xray_ip, port=int(xray_port))