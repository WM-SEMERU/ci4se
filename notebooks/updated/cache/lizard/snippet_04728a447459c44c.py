def raid_alert(self, status, used, available, type):
    if type == 'raid0':
        return 'OK'
    if status == 'inactive':
        return 'CRITICAL'
    if used is None or available is None:
        return 'DEFAULT'
    elif used < available:
        return 'WARNING'
    return 'OK'