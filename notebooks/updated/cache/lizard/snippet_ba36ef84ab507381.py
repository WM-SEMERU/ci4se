def extract(list_name, base_url, list_config=None, user=None, password=None):
    if not (base_url and list_name):
        raise RuntimeError('base_url [{}] and list_name [{}] can not be NULL'
            .format(base_url, list_name))
    list_config = list_config or {}
    assert isinstance(list_config, dict)
    logr.debug('[{}] {}: {}'.format(base_url, list_name, user))
    list_url = '{}/roster/{}'.format(base_url, list_name)
    content = _download(list_url, user, password)
    check_h2(content, 'Error')
    users = re.findall('(?<=>)(\\S* at \\S*|\\S*@\\S*)(?=<\\/a>)', content)
    users = [('@'.join(u.split(' at ')) if ' at ' in u else u) for u in users]
    return users