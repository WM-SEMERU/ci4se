def ids2marc(self, key, value):

    def _is_schema_inspire_bai(id_, schema):
        return schema == 'INSPIRE BAI'

    def _is_schema_inspire_id(id_, schema):
        return schema == 'INSPIRE ID'

    def _is_schema_spires(id_, schema):
        return schema == 'SPIRES'

    def _is_schema_linkedin(id, schema):
        return schema == 'LINKEDIN'

    def _is_schema_twitter(id, schema):
        return schema == 'TWITTER'
    id_ = value.get('value')
    schema = value.get('schema')
    if _is_schema_spires(id_, schema):
        self.setdefault('970', []).append({'a': id_})
    elif _is_schema_linkedin(id_, schema):
        self.setdefault('8564', []).append({'u':
            'https://www.linkedin.com/in/{id}'.format(id=quote_url(id_)),
            'y': 'LINKEDIN'})
    elif _is_schema_twitter(id_, schema):
        self.setdefault('8564', []).append({'u': 'https://twitter.com/{id}'
            .format(id=id_), 'y': 'TWITTER'})
    elif _is_schema_inspire_id(id_, schema):
        return {'a': id_, '9': 'INSPIRE'}
    elif _is_schema_inspire_bai(id_, schema):
        return {'a': id_, '9': 'BAI'}
    else:
        return {'a': id_, '9': schema}