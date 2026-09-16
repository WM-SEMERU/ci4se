def proper_case(package_name):
    r = _get_requests_session().get('https://pypi.org/pypi/{0}/json'.format
        (package_name), timeout=0.3, stream=True)
    if not r.ok:
        raise IOError('Unable to find package {0} in PyPI repository.'.
            format(package_name))
    r = parse.parse('https://pypi.org/pypi/{name}/json', r.url)
    good_name = r['name']
    return good_name