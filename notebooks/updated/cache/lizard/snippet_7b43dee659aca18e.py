def replication_group_exists(name, region=None, key=None, keyid=None,
    profile=None):
    return bool(describe_replication_groups(name=name, region=region, key=
        key, keyid=keyid, profile=profile))