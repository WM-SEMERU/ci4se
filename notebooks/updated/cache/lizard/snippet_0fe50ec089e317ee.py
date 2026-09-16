def get_harddisk_sleep():
    ret = salt.utils.mac_utils.execute_return_result(
        'systemsetup -getharddisksleep')
    return salt.utils.mac_utils.parse_return(ret)