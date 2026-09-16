def _get_json(value):
    if hasattr(value, 'replace'):
        value = value.replace('\n', ' ')
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        if hasattr(value, 'replace'):
            value = value.replace('"', '\\"')
        return json.loads('"{}"'.format(value))