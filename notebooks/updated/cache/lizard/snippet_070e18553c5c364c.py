def record_get_details(object_id, input_params={}, always_retry=True, **kwargs
    ):
    return DXHTTPRequest('/%s/getDetails' % object_id, input_params,
        always_retry=always_retry, **kwargs)