def fix_auth_url_version_prefix(auth_url):
    auth_url = _augment_url_with_version(auth_url)
    url_fixed = False
    if get_keystone_version() >= 3 and has_in_url_path(auth_url, ['/v2.0']):
        url_fixed = True
        auth_url = url_path_replace(auth_url, '/v2.0', '/v3', 1)
    return auth_url, url_fixed