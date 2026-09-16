def render(json_data, saltenv='base', sls='', **kws):
    if not isinstance(json_data, six.string_types):
        json_data = json_data.read()
    if json_data.startswith('#!'):
        json_data = json_data[json_data.find('\n') + 1:]
    if not json_data.strip():
        return {}
    return json.loads(json_data)