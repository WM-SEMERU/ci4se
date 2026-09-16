def set_remote_events(enable):
    state = __utils__['mac_utils.validate_enabled'](enable)
    cmd = 'systemsetup -setremoteappleevents {0}'.format(state)
    __utils__['mac_utils.execute_return_success'](cmd)
    return __utils__['mac_utils.confirm_updated'](state, get_remote_events,
        normalize_ret=True)