def delete_request(self, container, resource=None, query_items=None, accept
    =None):
    url = self.make_url(container, resource)
    headers = self._make_headers(accept)
    if query_items and isinstance(query_items, (list, tuple, set)):
        url += RestHttp._list_query_str(query_items)
        query_items = None
    try:
        rsp = requests.delete(url, params=query_items, headers=headers,
            verify=self._verify, timeout=self._timeout)
    except requests.exceptions.ConnectionError as e:
        RestHttp._raise_conn_error(e)
    if self._dbg_print:
        self.__print_req('DELETE', rsp.url, headers, None)
    return self._handle_response(rsp)