def _divide_filter_args(self, filter_args):
    query_parms = []
    client_filter_args = {}
    if filter_args is not None:
        for prop_name in filter_args:
            prop_match = filter_args[prop_name]
            if prop_name in self._query_props:
                self._append_query_parms(query_parms, prop_name, prop_match)
            else:
                client_filter_args[prop_name] = prop_match
    query_parms_str = '&'.join(query_parms)
    if query_parms_str:
        query_parms_str = '?{}'.format(query_parms_str)
    return query_parms_str, client_filter_args