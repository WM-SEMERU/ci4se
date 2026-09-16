def filter_by(self, text=(), types=(), units=(), include_unset=False):
    if not (isinstance(text, Sequence) and all(isinstance(phrase,
        string_types) for phrase in text)):
        raise TypeError('text should be sequence of strings')
    values = [self.__values[name] for name in self.__filter.filter_by(types
        =types, units=units) if include_unset or not self.__values[name].unset
        ] if types or units else self.__values
    if text:
        if isinstance(text, string_types):
            text = ensure_unicode(text),
        text = [phrase.lower() for phrase in text]
        new_values = []
        for value in values:
            label = value.label.lower()
            description = value.description.lower(
                ) if value.description else ''
            if any(phrase in label or description and phrase in description for
                phrase in text):
                new_values.append(value)
        values = new_values
    return values