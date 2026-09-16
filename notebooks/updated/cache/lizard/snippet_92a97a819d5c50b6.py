def delete_hosted_zone_by_domain(Name, PrivateZone=None, region=None, key=
    None, keyid=None, profile=None):
    args = {'Name': Name, 'PrivateZone': PrivateZone, 'region': region,
        'key': key, 'keyid': keyid, 'profile': profile}
    zone = find_hosted_zone(**args)
    if not zone:
        log.error("Couldn't resolve domain name %s to a hosted zone ID.", Name)
        return False
    Id = zone[0]['HostedZone']['Id']
    return delete_hosted_zone(Id=Id, region=region, key=key, keyid=keyid,
        profile=profile)