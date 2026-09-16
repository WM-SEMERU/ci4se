def increase_volume(percentage):
    if percentage > 100 or percentage < 0:
        raise ValueError('percentage must be an integer between 0 and 100')
    if system.get_name() == 'windows':
        pass
    elif system.get_name() == 'mac':
        volume_int = percentage / 10
        old_volume = get()
        new_volume = old_volume + volume_int
        if new_volume > 10:
            new_volume = 10
        set_volume(new_volume * 10)
    else:
        formatted = '%d%%+' % percentage
        sp.Popen(['amixer', '--quiet', 'sset', 'Master', formatted]).wait()