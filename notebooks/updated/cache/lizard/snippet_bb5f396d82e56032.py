def _load_architectures(self, family):
    if 'architectures' not in family:
        raise InternalError(
            'required architectures key not in build_settings.json for desired family'
            )
    for key, val in family['architectures'].items():
        if not isinstance(val, dict):
            raise InternalError(
                'All entries under chip_settings must be dictionaries')
        self.archs[key] = deepcopy(val)