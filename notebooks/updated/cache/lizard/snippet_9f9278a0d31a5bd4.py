def list_elbs(region=None, key=None, keyid=None, profile=None):
    return [e.name for e in get_all_elbs(region=region, key=key, keyid=
        keyid, profile=profile)]