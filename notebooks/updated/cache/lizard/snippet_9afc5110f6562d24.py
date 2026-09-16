def _create_and_send_json_bulk(self, payload, req_url, request_type='POST'):
    ct_header = {'Content-Type': 'application/json; charset=utf-8'}
    try:
        json_pl = json.dumps(payload)
    except TypeError as err:
        raise CraftAiBadRequestError(
            'Error while dumping the payload into jsonformat when converting it for the bulk request. {}'
            .format(err.__str__()))
    if request_type == 'POST':
        resp = self._requests_session.post(req_url, headers=ct_header, data
            =json_pl)
    elif request_type == 'DELETE':
        resp = self._requests_session.delete(req_url, headers=ct_header,
            data=json_pl)
    else:
        raise CraftAiBadRequestError(
            'Request for the bulk API should be either a POST or DELETErequest'
            )
    agents = self._decode_response(resp)
    agents = self._decode_response_bulk(agents)
    return agents