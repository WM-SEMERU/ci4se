def complete_request(self, account_id, request_id, **params):
    response = self._post('v2', 'accounts', account_id, 'transactions',
        request_id, 'complete', data=params)
    return self._make_api_object(response, APIObject)