def view_set(method_name):

    def view_set(value, context, **_params):
        method = getattr(context['view'], method_name)
        return _set(method, context['key'], value, (), {})
    return view_set