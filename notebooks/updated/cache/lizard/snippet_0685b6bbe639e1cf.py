def add_oid_entry(self, oid, type, value, label=None):
    if self.debug:
        print('DEBUG: %s %s %s %s' % (oid, type, value, label))
    item = {'type': str(type), 'value': str(value)}
    if label is not None:
        item['label'] = str(label)
    self.pending[oid] = item