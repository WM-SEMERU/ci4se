def list_all_zones_by_id(region=None, key=None, keyid=None, profile=None):
    ret = describe_hosted_zones(region=region, key=key, keyid=keyid,
        profile=profile)
    return [r['Id'].replace('/hostedzone/', '') for r in ret]