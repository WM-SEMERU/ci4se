def _severity_by_name(name):
    for intvalue, sevname in SEVERITY.items():
        if name.lower() == sevname:
            return intvalue
    return 1