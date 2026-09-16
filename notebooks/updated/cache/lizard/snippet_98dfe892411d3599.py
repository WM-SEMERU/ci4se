def set_cache_value(self, name, value):
    dev_info = self.json_state.get('deviceInfo')
    if dev_info.get(name.lower()) is None:
        logger.error('Could not set %s for %s (key does not exist).', name,
            self.name)
        logger.error('- dictionary %s', dev_info)
        return
    dev_info[name.lower()] = str(value)