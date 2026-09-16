def show_image(kwargs, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The show_image function must be called with -f or --function.')
    items = query(action='template', command=kwargs['image'])
    if 'error' in items:
        return items['error']
    ret = {}
    for item in items:
        ret.update({item.attrib['name']: item.attrib})
    return ret