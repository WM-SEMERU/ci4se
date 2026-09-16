def project_move(object_id, input_params={}, always_retry=False, **kwargs):
    return DXHTTPRequest('/%s/move' % object_id, input_params, always_retry
        =always_retry, **kwargs)