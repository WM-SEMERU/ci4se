def compliance_report(data, *models, **kwargs):
    if isinstance(models, tuple) and isinstance(models[0], list):
        models = models[0]
    filepath = kwargs.pop('filepath', '')
    root = _get_root_object(models)
    root.load_dict(data)
    return root.compliance_report(filepath)