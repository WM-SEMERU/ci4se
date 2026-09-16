def config_changed(inherit_napalm_device=None, **kwargs):
    is_config_changed = False
    reason = ''
    try_compare = compare_config(inherit_napalm_device=napalm_device)
    if try_compare.get('result'):
        if try_compare.get('out'):
            is_config_changed = True
        else:
            reason = 'Configuration was not changed on the device.'
    else:
        reason = try_compare.get('comment')
    return is_config_changed, reason