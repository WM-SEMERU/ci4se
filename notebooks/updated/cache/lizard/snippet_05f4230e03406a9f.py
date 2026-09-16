def querysets_from_title_prefix(title_prefix=None, model=DEFAULT_MODEL, app
    =DEFAULT_APP):
    if title_prefix is None:
        title_prefix = [None]
    filter_dicts = []
    model_list = []
    if isinstance(title_prefix, basestring):
        title_prefix = title_prefix.split(',')
    elif not isinstance(title_prefix, dict):
        title_prefix = title_prefix
    if isinstance(title_prefix, (list, tuple)):
        for i, title_prefix in enumerate(title_prefix):
            if isinstance(title_prefix, basestring):
                if title_prefix.lower().endswith('sales'):
                    title_prefix = title_prefix[:-5].strip('_')
                    title_prefix += [title_prefix]
                    model_list += ['WikiItem']
                else:
                    model_list += [DEFAULT_MODEL]
            filter_dicts += [{'model__startswith': title_prefix}]
    elif isinstance(title_prefix, dict):
        filter_dicts = [title_prefix]
    elif isinstance(title_prefix, (list, tuple)):
        filter_dicts = util.listify(title_prefix)
    model = get_model(model, app)
    querysets = []
    for filter_dict, model in zip(filter_dicts, model_list):
        filter_dict = filter_dict or {}
        querysets += [model.objects.filter(**filter_dict)]