def _get_info_score(info):
    search = re.search(pattern='score (?P<eval>\\w+) (?P<value>-?\\d+)',
        string=info)
    return {'score': {'eval': search.group('eval'), 'value': int(search.
        group('value'))}}