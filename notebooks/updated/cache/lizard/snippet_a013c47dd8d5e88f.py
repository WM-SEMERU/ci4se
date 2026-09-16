def list_protocols(profile, **libcloud_kwargs):
    conn = _get_driver(profile=profile)
    libcloud_kwargs = salt.utils.args.clean_kwargs(**libcloud_kwargs)
    return conn.list_protocols(**libcloud_kwargs)