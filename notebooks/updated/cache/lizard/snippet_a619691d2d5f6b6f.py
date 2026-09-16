def print_sorted_device_list(self, device_list=None, sort_key='sn'):
    dev_list = (device_list if device_list is not None else self.
        get_all_devices_in_portal())
    sorted_dev_list = []
    if sort_key == 'sn':
        sort_keys = [k[sort_key] for k in dev_list if k[sort_key] is not None]
        sort_keys = sorted(sort_keys)
        for key in sort_keys:
            sorted_dev_list.extend([d for d in dev_list if d['sn'] == key])
    elif sort_key == 'name':
        sort_keys = [k['info']['description'][sort_key] for k in dev_list if
            k['info']['description'][sort_key] is not None]
        sort_keys = sorted(sort_keys)
        for key in sort_keys:
            sorted_dev_list.extend([d for d in dev_list if d['info'][
                'description'][sort_key] == key])
    elif sort_key == 'portals_aliases':
        sort_keys = [k[sort_key] for k in dev_list if k[sort_key] is not None]
        sort_keys = sorted(sort_keys)
        for key in sort_keys:
            sorted_dev_list.extend([d for d in dev_list if d[sort_key] == key])
    else:
        print('Sort key {!r} not recognized.'.format(sort_key))
        sort_keys = None
    self.print_device_list(device_list=sorted_dev_list)