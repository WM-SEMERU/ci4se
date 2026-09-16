def get_initkwargs(cls, form_list, initial_dict=None, instance_dict=None,
    condition_dict=None, *args, **kwargs):
    kwargs.update({'initial_dict': initial_dict or {}, 'instance_dict': 
        instance_dict or {}, 'condition_dict': condition_dict or {}})
    init_form_list = SortedDict()
    assert len(form_list) > 0, 'at least one form is needed'
    for i, form in enumerate(form_list):
        if isinstance(form, (list, tuple)):
            init_form_list[unicode(form[0])] = form[1]
        else:
            init_form_list[unicode(i)] = form
    for form in init_form_list.itervalues():
        if issubclass(form, formsets.BaseFormSet):
            form = form.form
        for field in form.base_fields.itervalues():
            if isinstance(field, forms.FileField) and not hasattr(cls,
                'file_storage'):
                raise NoFileStorageConfigured
    kwargs['form_list'] = init_form_list
    return kwargs