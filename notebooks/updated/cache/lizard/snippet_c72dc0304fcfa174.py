def set_section_config(self, section, content):
    if not self._config.has_section(section):
        self._config.add_section(section)
    for key in content:
        if isinstance(content[key], bool):
            content[key] = str(content[key]).lower()
        self._config.set(section, key, content[key])
    self._override_config[section] = content