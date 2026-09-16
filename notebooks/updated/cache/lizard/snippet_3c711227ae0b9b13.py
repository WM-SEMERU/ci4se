def list_all(self, environment_id, pagination):
    uri = 'api/pools/'
    data = dict()
    data['start_record'] = pagination.start_record
    data['end_record'] = pagination.end_record
    data['asorting_cols'] = pagination.asorting_cols
    data['searchable_columns'] = pagination.searchable_columns
    data['custom_search'] = pagination.custom_search or None
    data['environment_id'] = environment_id or None
    return self.post(uri, data=data)