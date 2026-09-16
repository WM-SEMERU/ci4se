def SetPreferredLanguageIdentifier(self, language_identifier):
    if not isinstance(language_identifier, py2to3.STRING_TYPES):
        raise ValueError('Language identifier is not a string.')
    values = language_ids.LANGUAGE_IDENTIFIERS.get(language_identifier.
        lower(), None)
    if not values:
        raise KeyError('Language identifier: {0:s} is not defined.'.format(
            language_identifier))
    self._language_identifier = language_identifier
    self._lcid = values[0]