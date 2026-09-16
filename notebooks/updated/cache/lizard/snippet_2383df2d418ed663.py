def analysis_set_properties(object_id, input_params={}, always_retry=True,
    **kwargs):
    return DXHTTPRequest('/%s/setProperties' % object_id, input_params,
        always_retry=always_retry, **kwargs)