def blend_vars(secrets, opt):
    base_obj = load_vars(opt)
    merged = merge_dicts(base_obj, secrets)
    template_obj = dict((k, v) for k, v in iteritems(merged) if v)
    template_obj['aomi_items'] = template_obj.copy()
    return template_obj