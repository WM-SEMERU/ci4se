def _get_distinct_hostnames(self):
    hostnames = []
    for section in self.sections:
        hostnames.extend(self._group_get_hostnames(section['name']))
    return set(hostnames)