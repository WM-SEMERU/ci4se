def get_next_id_for(self, key):
    portal_type = key.split('-')[0]
    config = get_config(None, portal_type=portal_type)
    id_template = config.get('form', '')
    number = self.storage.get(key) + 1
    spec = {'seq': number, 'alpha': Alphanumber(number), 'year':
        get_current_year(), 'parent_analysisrequest': 'ParentAR',
        'parent_ar_id': 'ParentARId', 'sampleType': key.replace(portal_type,
        '').strip('-')}
    return id_template.format(**spec)