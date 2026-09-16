def apply_extra_context(extra_context, context):
    for key, value in six.iteritems(extra_context):
        if callable(value):
            context[key] = value()
        else:
            context[key] = value