def _SanitizeField(self, field):
    if self._FIELD_DELIMITER and isinstance(field, py2to3.STRING_TYPES):
        return field.replace(self._FIELD_DELIMITER, ' ')
    return field