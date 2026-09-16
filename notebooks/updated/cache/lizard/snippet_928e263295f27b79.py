def _find_unpurge_targets(desired, **kwargs):
    return [x for x in desired if x in __salt__['pkg.list_pkgs'](
        purge_desired=True, **kwargs)]