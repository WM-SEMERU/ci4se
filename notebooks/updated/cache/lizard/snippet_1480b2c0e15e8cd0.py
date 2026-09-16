def has_alias(self, header):
    try:
        return self._limits[self.plugin_name + '_' + header.lower() + '_' +
            'alias'][0]
    except (KeyError, IndexError):
        return None