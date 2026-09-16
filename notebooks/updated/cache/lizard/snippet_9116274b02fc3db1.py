def describe(profile, description):
    api_type = description.pop('type', 'core')
    api = getattr(profile, api_type)
    return refine(api.query, description)