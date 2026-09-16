def workflow_update(object_id, input_params={}, always_retry=True, **kwargs):
    return DXHTTPRequest('/%s/update' % object_id, input_params,
        always_retry=always_retry, **kwargs)