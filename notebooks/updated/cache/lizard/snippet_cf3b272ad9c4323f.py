def create_data_disk(vm_=None, linode_id=None, data_size=None):
    r
    kwargs = {}
    kwargs.update({'LinodeID': linode_id, 'Label': vm_['name'] + '_data',
        'Type': 'ext4', 'Size': data_size})
    result = _query('linode', 'disk.create', args=kwargs)
    return _clean_data(result)