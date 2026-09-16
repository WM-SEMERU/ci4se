def list_locations(profile, **libcloud_kwargs):
    conn = _get_driver(profile=profile)
    libcloud_kwargs = salt.utils.args.clean_kwargs(**libcloud_kwargs)
    locations = conn.list_locations(**libcloud_kwargs)
    ret = []
    for loc in locations:
        ret.append(_simple_location(loc))
    return ret