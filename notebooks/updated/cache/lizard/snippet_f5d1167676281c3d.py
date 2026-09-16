def _normalize_number_values(self, parameters):
    for key, value in parameters.items():
        if isinstance(value, (int, float)):
            parameters[key] = str(Decimal(value).normalize(self._context))