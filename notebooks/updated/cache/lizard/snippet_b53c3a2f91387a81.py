def _parse_local_interface(self, config):
    match = re.search('local-interface (\\w+)', config)
    value = match.group(1) if match else None
    return dict(local_interface=value)