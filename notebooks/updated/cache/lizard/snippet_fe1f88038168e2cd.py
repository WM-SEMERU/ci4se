def all_required_fields(self):

    def required_check(f):
        return not is_nullable_type(f.data_type) and not f.has_default
    return self._filter_fields(required_check)