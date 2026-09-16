def _pylxd_model_to_dict(obj):
    marshalled = {}
    for key in obj.__attributes__.keys():
        if hasattr(obj, key):
            marshalled[key] = getattr(obj, key)
    return marshalled