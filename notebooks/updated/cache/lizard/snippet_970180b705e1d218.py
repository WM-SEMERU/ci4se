def validate_catalog(self, catalog=None, only_errors=False, fmt='dict',
    export_path=None):
    catalog = catalog or self
    return validation.validate_catalog(catalog, only_errors, fmt,
        export_path, validator=self.validator)