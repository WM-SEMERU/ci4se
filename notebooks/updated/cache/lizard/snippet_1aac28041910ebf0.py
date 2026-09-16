def get_composite_field_value(self, name):
    field = self.composite_fields[name]
    if hasattr(field, 'get_form'):
        return self.forms[name]
    if hasattr(field, 'get_formset'):
        return self.formsets[name]