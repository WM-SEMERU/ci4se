def parse_napp(napp_id):
    regex = '([a-zA-Z][a-zA-Z0-9_]{2,})/([a-zA-Z][a-zA-Z0-9_]{2,}):?(.+)?'
    compiled_regex = re.compile(regex)
    matched = compiled_regex.fullmatch(napp_id)
    if not matched:
        msg = '"{}" NApp has not the form username/napp_name[:version].'
        raise KytosException(msg.format(napp_id))
    return matched.groups()