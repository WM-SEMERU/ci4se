def view_attr(attr_name):

    def view_attr(value, context, **_params):
        setattr(context['view'], attr_name, value)
        return _attr()
    return view_attr