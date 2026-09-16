def get_date():
    ret = salt.utils.mac_utils.execute_return_result('systemsetup -getdate')
    return salt.utils.mac_utils.parse_return(ret)