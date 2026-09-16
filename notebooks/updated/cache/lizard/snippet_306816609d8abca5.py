def _init_records(self, record_types):
    for record_type in record_types:
        if str(record_type) not in self._my_map['recordTypeIds']:
            record_initialized = self._init_record(str(record_type))
            if record_initialized:
                self._my_map['recordTypeIds'].append(str(record_type))