def _get_model_form_field(model, name, formfield_callback=None, **kwargs):
    field = model._meta.get_field(name)
    if not field.editable:
        return None
    if formfield_callback is None:
        formfield = field.formfield(**kwargs)
    elif not callable(formfield_callback):
        raise TypeError('formfield_callback must be a function or callable')
    else:
        formfield = formfield_callback(field, **kwargs)
    return formfield