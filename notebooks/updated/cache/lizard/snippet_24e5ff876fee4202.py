def delete_key_pair(name, profile, **libcloud_kwargs):
    conn = _get_driver(profile=profile)
    libcloud_kwargs = salt.utils.args.clean_kwargs(**libcloud_kwargs)
    key = conn.get_key_pair(name)
    return conn.delete_key_pair(key, **libcloud_kwargs)