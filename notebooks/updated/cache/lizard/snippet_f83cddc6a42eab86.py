def create_attach_volumes(name, kwargs, call=None):
    if call != 'action':
        raise SaltCloudSystemExit(
            'The create_attach_volumes action must be called with -a or --action.'
            )
    volumes = literal_eval(kwargs['volumes'])
    node = kwargs['node']
    conn = get_conn()
    node_data = _expand_node(conn.ex_get_node(node))
    letter = ord('a') - 1
    for idx, volume in enumerate(volumes):
        volume_name = '{0}-sd{1}'.format(name, chr(letter + 2 + idx))
        volume_dict = {'disk_name': volume_name, 'location': node_data[
            'extra']['zone']['name'], 'size': volume['size'], 'type':
            volume.get('type', 'pd-standard'), 'image': volume.get('image',
            None), 'snapshot': volume.get('snapshot', None), 'auto_delete':
            volume.get('auto_delete', False)}
        create_disk(volume_dict, 'function')
        attach_disk(name, volume_dict, 'action')