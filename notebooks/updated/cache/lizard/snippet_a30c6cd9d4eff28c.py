def allowed(name, collection='all'):
    if not valid(name):
        return False
    blacklist = names()
    for forbidden in blacklist[collection]:
        if name.lower() == forbidden.lower():
            return False
        if forbidden.endswith('*'):
            if name.lower().startswith(forbidden[:-1].lower()):
                return False
        if forbidden.startswith('/'):
            if not allowed(name, collection=forbidden[1:]):
                return False
    return True