def mom_version_less_than(version, name='marathon-user'):
    if service_available_predicate(name):
        return mom_version() < LooseVersion(version)
    else:
        print('WARN: {} MoM not found. mom_version_less_than({}) is False'.
            format(name, version))
        return False