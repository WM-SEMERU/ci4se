def _parse_mode(self, config):
    value = re.search('switchport mode (\\w+)', config, re.M)
    return dict(mode=value.group(1))