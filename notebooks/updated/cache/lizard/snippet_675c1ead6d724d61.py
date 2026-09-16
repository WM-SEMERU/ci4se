def get_scope(self, scope_name):
    request_url = self._build_url(['Scope', scope_name])
    return self._do_request('GET', request_url)