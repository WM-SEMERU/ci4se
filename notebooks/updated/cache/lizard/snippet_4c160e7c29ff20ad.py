def project_describe(object_id, input_params={}, always_retry=True, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params,
        always_retry=always_retry, **kwargs)