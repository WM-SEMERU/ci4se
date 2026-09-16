def funding_info(self, key, value):
    return {'agency': value.get('a'), 'grant_number': value.get('c'),
        'project_number': value.get('f')}