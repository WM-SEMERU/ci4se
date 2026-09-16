def execute(self, sources, target):
    fields = self._get_fields_list_from_eps(sources)
    feature_set = set(self.feature_names)
    target._ml_fields = list(self._add_field_roles(fields[0], feature_set,
        self.role, self.augment))