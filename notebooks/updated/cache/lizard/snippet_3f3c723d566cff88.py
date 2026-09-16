def assign_account_entitlement_for_user(self, body, user_id,
    dont_notify_user=None, origin=None):
    route_values = {}
    if user_id is not None:
        route_values['userId'] = self._serialize.url('user_id', user_id, 'str')
    query_parameters = {}
    if dont_notify_user is not None:
        query_parameters['dontNotifyUser'] = self._serialize.query(
            'dont_notify_user', dont_notify_user, 'bool')
    if origin is not None:
        query_parameters['origin'] = self._serialize.query('origin', origin,
            'str')
    content = self._serialize.body(body, 'AccountEntitlementUpdateModel')
    response = self._send(http_method='PUT', location_id=
        '6490e566-b299-49a7-a4e4-28749752581f', version='5.0-preview.1',
        route_values=route_values, query_parameters=query_parameters,
        content=content)
    return self._deserialize('AccountEntitlement', response)