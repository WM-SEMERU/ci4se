def DisableInterfaces(interface):
    set_tested_versions = ['vista', '2008']
    set_args = ['/c', 'netsh', 'set', 'interface', interface, 'DISABLED']
    host_version = platform.platform().lower()
    for version in set_tested_versions:
        if host_version.find(version) != -1:
            res = client_utils_common.Execute('cmd', set_args, time_limit=-
                1, bypass_whitelist=True)
            return res
    return '', 'Command not available for this version.', 99, ''