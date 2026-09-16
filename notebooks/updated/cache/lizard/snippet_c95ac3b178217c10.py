def change_resource_record_sets(HostedZoneId=None, Name=None, PrivateZone=
    None, ChangeBatch=None, region=None, key=None, keyid=None, profile=None):
    if not _exactly_one((HostedZoneId, Name)):
        raise SaltInvocationError(
            'Exactly one of either HostZoneId or Name must be provided.')
    if Name:
        args = {'Name': Name, 'region': region, 'key': key, 'keyid': keyid,
            'profile': profile}
        args.update({'PrivateZone': PrivateZone}
            ) if PrivateZone is not None else None
        zone = find_hosted_zone(**args)
        if not zone:
            log.error("Couldn't resolve domain name %s to a hosted zone ID.",
                Name)
            return []
        HostedZoneId = zone[0]['HostedZone']['Id']
    args = {'HostedZoneId': HostedZoneId, 'ChangeBatch':
        _aws_encode_changebatch(ChangeBatch)}
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    tries = 20
    while tries:
        try:
            r = conn.change_resource_record_sets(**args)
            return _wait_for_sync(r['ChangeInfo']['Id'], conn, 30)
        except ClientError as e:
            if tries and e.response.get('Error', {}).get('Code'
                ) == 'Throttling':
                log.debug('Throttled by AWS API.')
                time.sleep(3)
                tries -= 1
                continue
            log.error(
                'Failed to apply requested changes to the hosted zone %s: %s',
                Name or HostedZoneId, six.text_type(e))
            raise e
    return False