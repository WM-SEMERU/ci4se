def _check_cron(user, path, mask, cmd):
    arg_mask = mask.split(',')
    arg_mask.sort()
    lst = __salt__['incron.list_tab'](user)
    for cron in lst['crons']:
        if path == cron['path'] and cron['cmd'] == cmd:
            cron_mask = cron['mask'].split(',')
            cron_mask.sort()
            if cron_mask == arg_mask:
                return 'present'
            if any([(x in cron_mask) for x in arg_mask]):
                return 'update'
    return 'absent'