def _get_default_values(self, default_values=None):
    if not default_values:
        default_values = self.DEFAULT_VALUES
    if default_values:
        api_version = str(self._connection._apiVersion)
        values = default_values.get(api_version, {}).copy()
    else:
        values = {}
    return values