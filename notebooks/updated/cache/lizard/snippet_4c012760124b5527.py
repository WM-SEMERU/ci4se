def get_sections(self, s, base, sections=['Parameters', 'Other Parameters']):
    params = self.params
    s = self._remove_summary(s)
    for section in sections:
        key = '%s.%s' % (base, section.lower().replace(' ', '_'))
        params[key] = self._get_section(s, section)
    return s