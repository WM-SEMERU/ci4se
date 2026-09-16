def _get_org(aff):
    try:
        org = aff['organization']
        if not isinstance(org, str):
            try:
                org = org['$']
            except TypeError:
                org = ', '.join([d['$'] for d in org if d])
    except KeyError:
        org = None
    return org