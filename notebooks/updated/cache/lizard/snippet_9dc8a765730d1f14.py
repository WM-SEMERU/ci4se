def api_column_add(self, col_name):
    log.warning('This API is deprecated and will be removed on 1.15.X')
    filter_rel_fields = None
    if self.add_form_query_rel_fields:
        filter_rel_fields = self.add_form_query_rel_fields.get(col_name)
    ret_json = self._get_related_column_data(col_name, filter_rel_fields)
    response = make_response(ret_json, 200)
    response.headers['Content-Type'] = 'application/json'
    return response