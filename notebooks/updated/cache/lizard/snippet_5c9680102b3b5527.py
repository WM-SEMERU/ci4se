def is_exported(bundle):
    if not ckan:
        raise EnvironmentError(MISSING_CREDENTIALS_MSG)
    params = {'q': 'name:{}'.format(bundle.dataset.vid.lower())}
    resp = ckan.action.package_search(**params)
    return len(resp['results']) > 0