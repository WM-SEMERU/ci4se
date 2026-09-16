def update(name=None, pkgs=None, refresh=True, skip_verify=False, normalize
    =True, minimal=False, obsoletes=False, **kwargs):
    return upgrade(name, pkgs, refresh, skip_verify, normalize, minimal,
        obsoletes, **kwargs)