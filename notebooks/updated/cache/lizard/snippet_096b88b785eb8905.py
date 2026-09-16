def request(self, method, params=None, query_continue=None, files=None,
    auth=None, continuation=False):
    normal_params = _normalize_params(params, query_continue)
    if continuation:
        return self._continuation(method, params=normal_params, auth=auth,
            files=files)
    else:
        return self._request(method, params=normal_params, auth=auth, files
            =files)