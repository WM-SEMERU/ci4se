def execute_sql(server_context, schema_name, sql, container_path=None,
    max_rows=None, sort=None, offset=None, container_filter=None,
    save_in_session=None, parameters=None, required_version=None, timeout=
    _default_timeout):
    url = server_context.build_url('query', 'executeSql.api',
        container_path=container_path)
    payload = {'schemaName': schema_name, 'sql': sql}
    if container_filter is not None:
        payload['containerFilter'] = container_filter
    if max_rows is not None:
        payload['maxRows'] = max_rows
    if offset is not None:
        payload['offset'] = offset
    if sort is not None:
        payload['query.sort'] = sort
    if save_in_session is not None:
        payload['saveInSession'] = save_in_session
    if parameters is not None:
        for key, value in parameters.items():
            payload['query.param.' + key] = value
    if required_version is not None:
        payload['apiVersion'] = required_version
    return server_context.make_request(url, payload, timeout=timeout)