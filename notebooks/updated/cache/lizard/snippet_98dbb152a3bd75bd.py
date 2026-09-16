def _is_pingable(ip):
    ping_cmd = ['ping', '-c', '5', '-W', '1', '-i', '0.2', ip]
    try:
        linux_utils.execute(ping_cmd, check_exit_code=True)
        return True
    except RuntimeError:
        LOG.warning('Cannot ping ip address: %s', ip)
        return False