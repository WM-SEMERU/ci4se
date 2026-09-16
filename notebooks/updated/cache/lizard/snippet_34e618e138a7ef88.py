def TXT(host, nameserver=None):
    dig = ['dig', '+short', six.text_type(host), 'TXT']
    if nameserver is not None:
        dig.append('@{0}'.format(nameserver))
    cmd = __salt__['cmd.run_all'](dig, python_shell=False)
    if cmd['retcode'] != 0:
        log.warning(
            "dig returned exit code '%s'. Returning empty list as fallback.",
            cmd['retcode'])
        return []
    return [i for i in cmd['stdout'].split('\n')]