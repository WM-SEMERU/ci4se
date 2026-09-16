def update(self, item_id, attributes, silent=False, hook=True):
    if not isinstance(attributes, dict):
        raise TypeError('Must be of type dict')
    attributes = json.dumps(attributes)
    return self.transport.PUT(body=attributes, type='application/json', url
        ='/item/%d%s' % (item_id, self.get_options(silent=silent, hook=hook)))