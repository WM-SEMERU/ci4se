def _parse_description(self, config):
    value = DESCRIPTION_RE.search(config).group('value')
    return dict(description=value)