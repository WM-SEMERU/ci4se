def get_daemons(self, daemon_name=None, daemon_type=None):
    if daemon_name is not None:
        sections = self._search_sections('daemon.%s' % daemon_name)
        if 'daemon.%s' % daemon_name in sections:
            return sections['daemon.' + daemon_name]
        return {}
    if daemon_type is not None:
        sections = self._search_sections('daemon.')
        for name, daemon in list(sections.items()):
            if 'type' not in daemon or not daemon['type'] == daemon_type:
                sections.pop(name)
        return sections
    return self._search_sections('daemon.')