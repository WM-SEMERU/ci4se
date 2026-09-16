def replacement_fields_from_context(context):
    return dict((k[3:].lower(), context[k]) for k in context if k.
        startswith('BE_'))