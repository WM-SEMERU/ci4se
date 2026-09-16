def _ParseInsserv(self, data):
    p = config_file.FieldParser()
    entries = p.ParseEntries(data)
    raw = {e[0]: e[1:] for e in entries}
    facilities = {}
    for k, v in iteritems(raw):
        k = k.replace('<', '').replace('>', '')
        facilities[k] = v
    for k, vals in iteritems(facilities):
        self.insserv[k] = []
        for v in vals:
            self.insserv[k].extend(self._InsservExpander(facilities, v))