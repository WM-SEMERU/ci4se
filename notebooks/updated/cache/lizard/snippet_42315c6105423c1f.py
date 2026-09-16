def POST(self, rest_path_list, **kwargs):
    fields = kwargs.pop('fields', None)
    if fields is not None:
        return self._send_mmp_stream('POST', rest_path_list, fields, **kwargs)
    else:
        return self._request('POST', rest_path_list, **kwargs)