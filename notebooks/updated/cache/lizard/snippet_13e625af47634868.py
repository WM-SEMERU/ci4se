def smart_search_vrf(self, auth, query_str, search_options=None,
    extra_query=None):
    if search_options is None:
        search_options = {}
    self._logger.debug('smart_search_vrf query string: %s' % query_str)
    success, query = self._parse_vrf_query(query_str)
    if not success:
        return {'interpretation': query, 'search_options': search_options,
            'result': [], 'error': True, 'error_message':
            'query interpretation failed'}
    if extra_query is not None:
        query = {'operator': 'and', 'val1': query, 'val2': extra_query}
    self._logger.debug('smart_search_vrf; query expanded to: %s' % unicode(
        query))
    search_result = self.search_vrf(auth, query, search_options)
    search_result['interpretation'] = query
    search_result['error'] = False
    return search_result