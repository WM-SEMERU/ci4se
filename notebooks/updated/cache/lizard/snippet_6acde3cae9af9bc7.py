def add_section(self, section, section_params):
    if section == None:
        raise Exception('Section name cannot be null')
    section = '' if self._is_shadow_name(section) else section
    if section_params == None or len(section_params) == 0:
        return
    for key, value in section_params.items():
        key = '' if self._is_shadow_name(key) else key
        if len(key) > 0 and len(section) > 0:
            key = section + '.' + key
        elif len(key) == 0:
            key = section
        self[key] = value