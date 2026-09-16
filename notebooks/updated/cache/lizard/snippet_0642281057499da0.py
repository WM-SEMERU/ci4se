def _parse_description(self, config):
    value = None
    match = re.search('description (.+)$', config, re.M)
    if match:
        value = match.group(1)
    return dict(description=value)