def workflow_set_visibility(object_id, input_params={}, always_retry=True,
    **kwargs):
    return DXHTTPRequest('/%s/setVisibility' % object_id, input_params,
        always_retry=always_retry, **kwargs)