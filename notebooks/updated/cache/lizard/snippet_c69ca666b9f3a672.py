def _validate_filter_fields(self, filter_by):
    for filter_field in filter_by:
        if (filter_field not in self.RESPONSE_FIELD_MAP or not self.
            RESPONSE_FIELD_MAP[filter_field].is_filter):
            raise InvalidFilterFieldException(
                '"{0}" is an invalid filter field'.format(filter_field))