def integration_and_config(self, path):
    if path.startswith(tuple(INTEGRATION_MAP.keys())):
        key = INTEGRATION_MAP[path.split(':')[0] + ':']
        integration = self._integrations.get(key)
        config = {}
        for sample in self._samples:
            config = tz.get_in(['config', key], sample)
            if config:
                break
        return integration, config
    return None, None