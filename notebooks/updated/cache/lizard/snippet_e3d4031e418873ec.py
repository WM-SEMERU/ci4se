def get_url_from_model_core(request, obj):
    from is_core.site import get_model_core
    model_core = get_model_core(obj.__class__)
    if model_core and hasattr(model_core, 'ui_patterns'):
        edit_pattern = model_core.ui_patterns.get('detail')
        return edit_pattern.get_url_string(request, obj=obj
            ) if edit_pattern and edit_pattern.has_permission('get',
            request, obj=obj) else None
    else:
        return None