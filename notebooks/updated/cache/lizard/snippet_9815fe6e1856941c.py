def event_update(self, event_id, name=None, season=None, start_time=None,
    event_group_id=None, status=None, account=None, **kwargs):
    assert isinstance(season, list)
    assert isinstance(start_time, datetime
        ), 'start_time needs to be a `datetime.datetime`'
    if not account:
        if 'default_account' in self.config:
            account = self.config['default_account']
    if not account:
        raise ValueError('You need to provide an account')
    account = Account(account)
    event = Event(event_id)
    op_data = {'fee': {'amount': 0, 'asset_id': '1.3.0'}, 'event_id': event
        ['id'], 'prefix': self.prefix}
    if event['status'] == status:
        status = None
    if event_group_id:
        if event_group_id[0] == '1':
            EventGroup(event_group_id)
        else:
            test_proposal_in_buffer(kwargs.get('append_to', self.propbuffer
                ), 'event_group_create', event_group_id)
        op_data.update({'new_event_group_id': event_group_id})
    if name:
        op_data.update({'new_name': name})
    if season:
        op_data.update({'new_season': season})
    if start_time:
        op_data.update({'new_start_time': formatTime(start_time)})
    if status:
        op_data.update({'new_status': status})
    op = operations.Event_update(**op_data)
    return self.finalizeOp(op, account['name'], 'active', **kwargs)