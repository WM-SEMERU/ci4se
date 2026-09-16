def create_ajaxable_view_from_model_inherit_parent_class(model_class,
    parent_class_list, operation='Create'):
    generic_module = importlib.import_module('django.views.generic')
    view_class_name = '%sView' % operation
    view_class = getattr(generic_module, view_class_name)
    parent_class_list.append(view_class)
    create_view_class = type('%s%s%s' % (model_class.__name__, operation,
        'View'), tuple(parent_class_list), {'model': model_class,
        'template_name': 'form_view_base_template.html',
        'submit_button_text': operation, 'success_url': '../'})
    return create_view_class