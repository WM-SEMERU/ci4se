def execution_environment():
    context = {}
    context['conf'] = config()
    if relation_id():
        context['reltype'] = relation_type()
        context['relid'] = relation_id()
        context['rel'] = relation_get()
    context['unit'] = local_unit()
    context['rels'] = relations()
    context['env'] = os.environ
    return context