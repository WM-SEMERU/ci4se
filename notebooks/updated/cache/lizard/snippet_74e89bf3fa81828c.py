def submit_statement_request(meth, end_point, query_str='', data=None,
    tries=2, **params):
    full_end_point = 'statements/' + end_point.lstrip('/')
    return make_db_rest_request(meth, full_end_point, query_str, data,
        params, tries)