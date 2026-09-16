def get_work_item_next_states_on_checkin_action(self, ids, action=None):
    query_parameters = {}
    if ids is not None:
        ids = ','.join(map(str, ids))
        query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
    if action is not None:
        query_parameters['action'] = self._serialize.query('action', action,
            'str')
    response = self._send(http_method='GET', location_id=
        'afae844b-e2f6-44c2-8053-17b3bb936a40', version='5.1-preview.1',
        query_parameters=query_parameters)
    return self._deserialize('[WorkItemNextStateOnTransition]', self.
        _unwrap_collection(response))