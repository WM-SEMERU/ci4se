def delete_tags(name, tags, region=None, key=None, keyid=None, profile=None):
    if exists(name, region, key, keyid, profile):
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        ret = _remove_tags(conn, name, tags)
        return ret
    else:
        return False