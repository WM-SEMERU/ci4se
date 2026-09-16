def _get_object_as_soft(self):
    soft = []
    if self.database is not None:
        soft.append(self.database._get_object_as_soft())
    soft += ['^%s = %s' % (self.geotype, self.name), self.
        _get_metadata_as_string()]
    for gsm in itervalues(self.gsms):
        soft.append(gsm._get_object_as_soft())
    for gpl in itervalues(self.gpls):
        soft.append(gpl._get_object_as_soft())
    return '\n'.join(soft)