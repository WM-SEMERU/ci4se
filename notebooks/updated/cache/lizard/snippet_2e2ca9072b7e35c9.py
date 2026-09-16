def database_close(object_id, input_params={}, always_retry=True, **kwargs):
    return DXHTTPRequest('/%s/close' % object_id, input_params,
        always_retry=always_retry, **kwargs)