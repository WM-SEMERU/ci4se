def get(sub_array_id):
    if not re.match('^subarray-0[0-9]|subarray-1[0-5]$', sub_array_id):
        response = dict(error=
            'Invalid sub-array ID specified "{}" does not match sub-array ID naming convention (ie. subarray-[00-15]).'
            .format(sub_array_id))
        return response, HTTPStatus.BAD_REQUEST
    if sub_array_id not in DB.get_sub_array_ids():
        response = dict(error=
            'Sub-array "{}" does not currently exist. Known sub-arrays = {}'
            .format(sub_array_id, DB.get_sub_array_ids()))
        return response, HTTPStatus.NOT_FOUND
    block_ids = DB.get_sub_array_sbi_ids(sub_array_id)
    _blocks = [b for b in DB.get_block_details(block_ids)]
    response = dict(scheduling_blocks=[])
    _url = get_root_url()
    for block in _blocks:
        block['links'] = {'self': '{}/scheduling-block/{}'.format(_url,
            block['id'])}
        response['scheduling_blocks'].append(block)
    response['links'] = {'self': '{}'.format(request.url), 'list':
        '{}/sub-arrays'.format(_url), 'home': '{}'.format(_url)}
    return response, HTTPStatus.OK