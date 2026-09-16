def bulk_insert(self, inserts, intervals=0, **kwargs):
    if None in inserts:
        inserts[time.time()] = inserts.pop(None)
    if self._write_func:
        for timestamp, names in inserts.iteritems():
            for name, values in names.iteritems():
                names[name] = [self._write_func(v) for v in values]
    self._batch_insert(inserts, intervals, **kwargs)