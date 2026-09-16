def _getInstrumentsVoc(self):
    cfilter = {'portal_type': 'Instrument', 'is_active': True}
    if self.getMethod():
        cfilter['getMethodUIDs'] = {'query': self.getMethod().UID(),
            'operator': 'or'}
    bsc = getToolByName(self, 'bika_setup_catalog')
    items = [('', 'No instrument')] + [(o.UID, o.Title) for o in bsc(cfilter)]
    o = self.getInstrument()
    if o and o.UID() not in [i[0] for i in items]:
        items.append((o.UID(), o.Title()))
    items.sort(lambda x, y: cmp(x[1], y[1]))
    return DisplayList(list(items))