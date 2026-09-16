def do_usufy(self, query, **kwargs):
    results = []
    test = self.check_usufy(query, **kwargs)
    if test:
        r = {'type': 'i3visio.profile', 'value': self.platformName + ' - ' +
            query, 'attributes': []}
        aux = {}
        aux['type'] = 'i3visio.uri'
        aux['value'] = self.createURL(word=query, mode='usufy')
        aux['attributes'] = []
        r['attributes'].append(aux)
        aux = {}
        aux['type'] = 'i3visio.alias'
        aux['value'] = query
        aux['attributes'] = []
        r['attributes'].append(aux)
        aux = {}
        aux['type'] = 'i3visio.platform'
        aux['value'] = self.platformName
        aux['attributes'] = []
        r['attributes'].append(aux)
        r['attributes'] += self.process_usufy(test)
        results.append(r)
    return results