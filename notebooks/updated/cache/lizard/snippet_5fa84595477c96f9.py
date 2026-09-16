def connect_to_cloudfiles(region=None, public=None):
    if public is None:
        is_public = not bool(get_setting('use_servicenet'))
    else:
        is_public = public
    ret = _create_client(ep_name='object_store', region=region, public=
        is_public)
    if ret:
        region = _safe_region(region)
        ret.cdn_management_url = _get_service_endpoint(None, 'object_cdn',
            region, public=is_public)
    return ret