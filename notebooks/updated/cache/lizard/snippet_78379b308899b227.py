def relative_ref(*parts):

    def relative_ref(_value, context, **_params):
        return reference.Relative(*(parts + (context['key'],)))
    return relative_ref