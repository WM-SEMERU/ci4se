def update(self, data):
    if not isinstance(data, list):
        data = [data]
    master = Handler.ALL_VERS_DATA
    for record in data:
        for k, v in iteritems(record):
            try:
                record[k] = int(v)
            except ValueError:
                record[k] = v
        try:
            label = record['label']
        except KeyError:
            raise ValueError(
                'Must provide a valid label argument.  Given:%s%s' % (os.
                linesep, ('%s  ' % os.linesep).join([('%15s:%s' % (k, v)) for
                k, v in iteritems(kwargs)])))
        try:
            masterLabel = master[label]
        except KeyError:
            master[label] = record
            self._updated = True
            continue
        for k, v in iteritems(record):
            try:
                if masterLabel[k] == v:
                    continue
            except KeyError:
                pass
            self._updated = True
            try:
                master[label].update(record)
            except KeyError:
                break