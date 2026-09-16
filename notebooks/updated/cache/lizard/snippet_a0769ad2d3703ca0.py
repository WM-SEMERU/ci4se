def get_field_min_max(self, name, **query_dict):
    param_dict = query_dict.copy()
    param_dict.update({'rows': 1, 'fl': name, 'sort': '%s asc' % name})
    try:
        min_resp_dict = self._post_query(**param_dict)
        param_dict['sort'] = '%s desc' % name
        max_resp_dict = self._post_query(**param_dict)
        return min_resp_dict['response']['docs'][0][name], max_resp_dict[
            'response']['docs'][0][name]
    except Exception:
        self._log.exception('Exception')
        raise