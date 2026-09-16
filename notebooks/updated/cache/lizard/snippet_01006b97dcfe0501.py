def set_change_request_state(change_id, state='approved'):
    client = _get_client()
    client.table = 'change_request'
    record = client.get({'number': change_id})
    if not record:
        log.error('Failed to fetch change record, maybe it does not exist?')
        return False
    sys_id = record[0]['sys_id']
    response = client.update({'approval': state}, sys_id)
    return response