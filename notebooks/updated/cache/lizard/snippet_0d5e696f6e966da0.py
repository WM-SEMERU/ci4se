def _load_records(self, record_type_idstrs):
    for record_type_idstr in record_type_idstrs:
        try:
            self._init_record(record_type_idstr)
        except (ImportError, KeyError):
            pass