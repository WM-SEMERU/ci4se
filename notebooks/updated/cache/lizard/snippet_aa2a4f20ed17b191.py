def deleteEndpoint(self, ep, cbfn=''):
    result = asyncResult(callback=cbfn)
    result.endpoint = ep
    data = self._deleteURL('/endpoints/' + ep)
    if data.status_code == 200:
        result.error = False
        result.is_done = True
    elif data.status_code == 202:
        self.database['async-responses'][json.loads(data.content)[
            'async-response-id']] = result
    else:
        result.error = response_codes('resource', data.status_code)
        result.is_done = True
    result.raw_data = data.content
    result.status_code = data.status_code
    return result