def set_description(self, description):
    self._description = validate_type(description, type(None), *six.
        string_types)