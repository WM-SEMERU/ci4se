def get_placeholder_data(self, request, obj=None):
    if not hasattr(self.model, '_meta_placeholder_fields'):
        return []
    data = []
    for name, field in self.model._meta_placeholder_fields.items():
        assert isinstance(field, PlaceholderField)
        data.append(PlaceholderData(slot=field.slot, title=field.
            verbose_name.capitalize(), fallback_language=None))
    return data