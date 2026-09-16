def database_set_details(object_id, input_params={}, always_retry=True, **
    kwargs):
    return DXHTTPRequest('/%s/setDetails' % object_id, input_params,
        always_retry=always_retry, **kwargs)