def schedule_enabled():
    cmd = ['softwareupdate', '--schedule']
    ret = salt.utils.mac_utils.execute_return_result(cmd)
    enabled = ret.split()[-1]
    return salt.utils.mac_utils.validate_enabled(enabled) == 'on'