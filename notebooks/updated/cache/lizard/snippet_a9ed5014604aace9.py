def database_add_tags(object_id, input_params={}, always_retry=True, **kwargs):
    return DXHTTPRequest('/%s/addTags' % object_id, input_params,
        always_retry=always_retry, **kwargs)