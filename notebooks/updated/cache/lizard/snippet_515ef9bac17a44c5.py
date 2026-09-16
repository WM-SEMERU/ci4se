def container_remove_folder(object_id, input_params={}, always_retry=False,
    **kwargs):
    return DXHTTPRequest('/%s/removeFolder' % object_id, input_params,
        always_retry=always_retry, **kwargs)