def get_language(self, language_code, site_id=None):
    if language_code is None:
        raise ValueError(get_null_language_error())
    if site_id is None:
        site_id = getattr(settings, 'SITE_ID', None)
    for lang_dict in self.get(site_id, ()):
        if lang_dict['code'] == language_code:
            return lang_dict
    for lang_dict in self.get(site_id, ()):
        if lang_dict['code'].split('-')[0] == language_code.split('-')[0]:
            return lang_dict
    return self['default']