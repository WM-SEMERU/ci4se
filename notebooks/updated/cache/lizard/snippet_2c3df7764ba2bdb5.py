async def list_state(self, request):
    paging_controls = self._get_paging_controls(request)
    head, root = await self._head_to_root(request.url.query.get('head', None))
    validator_query = client_state_pb2.ClientStateListRequest(state_root=
        root, address=request.url.query.get('address', None), sorting=self.
        _get_sorting_message(request, 'default'), paging=self.
        _make_paging_message(paging_controls))
    response = await self._query_validator(Message.
        CLIENT_STATE_LIST_REQUEST, client_state_pb2.ClientStateListResponse,
        validator_query)
    return self._wrap_paginated_response(request=request, response=response,
        controls=paging_controls, data=response.get('entries', []), head=head)