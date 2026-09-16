def set_hibernate_timeout(timeout, power='ac', scheme=None):
    return _set_powercfg_value(scheme=scheme, sub_group='SUB_SLEEP',
        setting_guid='HIBERNATEIDLE', power=power, value=timeout)