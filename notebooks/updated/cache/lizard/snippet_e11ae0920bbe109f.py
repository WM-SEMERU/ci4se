def get_form_bound_field(form, field_name):
    field = form.fields[field_name]
    field = field.get_bound_field(form, field_name)
    return field