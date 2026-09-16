def get_relay_ip_list(server=_DEFAULT_SERVER):
    ret = list()
    setting = 'RelayIpList'
    lines = _get_wmi_setting('IIsSmtpServerSetting', setting, server)
    if not lines:
        _LOG.debug('%s is empty: %s', setting, lines)
        if lines is None:
            lines = [None]
        return list(lines)
    i = 0
    while i < len(lines):
        octets = [six.text_type(x) for x in lines[i:i + 4]]
        address = '.'.join(octets)
        ret.append(address)
        i += 4
    return ret