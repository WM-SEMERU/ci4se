def parse_config_for_selected_keys(content, keys):
    config_items = {key: None for key in keys}
    if not content:
        return config_items, content
    stripped = content.strip()
    if len(stripped) == 0:
        return {}, None
    elif stripped[0] == '{':
        config = json.loads(content)
    else:
        config = yaml.load(content)
    if not isinstance(config, dict):
        raise ValueError('Invalid config.')
    for key in keys:
        config_items[key] = config.pop(key, None)
    if not config:
        return config_items, None
    if stripped[0] == '{':
        content_out = json.dumps(config, indent=4)
    else:
        content_out = yaml.dump(config, default_flow_style=False)
    return config_items, content_out