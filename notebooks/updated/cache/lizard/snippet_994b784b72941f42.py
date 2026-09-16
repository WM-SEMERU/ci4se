def view_get(method_name):

    def view_get(_value, context, **_params):
        method = getattr(context['view'], method_name)
        return _get(method, context['key'], (), {})
    return view_get