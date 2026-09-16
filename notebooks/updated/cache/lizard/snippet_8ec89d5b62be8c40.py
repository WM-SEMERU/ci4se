def create_record_sets(self, record_set_dicts):
    record_set_objects = []
    for record_set_dict in record_set_dicts:
        if record_set_dict.pop('Enabled', True):
            record_set_objects.append(self.create_record_set(record_set_dict))
    return record_set_objects