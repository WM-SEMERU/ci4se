def validate_create_package(package_format, owner, repo, **kwargs):
    client = get_packages_api()
    with catch_raise_api_exception():
        check = getattr(client, 
            'packages_validate_upload_%s_with_http_info' % package_format)
        _, _, headers = check(owner=owner, repo=repo, data=
            make_create_payload(**kwargs))
    ratelimits.maybe_rate_limit(client, headers)
    return True