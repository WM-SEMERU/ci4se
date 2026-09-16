def get_or_create_hosted_zone(client, zone_name):
    zone_id = get_hosted_zone_by_name(client, zone_name)
    if zone_id:
        return zone_id
    logger.debug('Zone %s does not exist, creating.', zone_name)
    reference = uuid.uuid4().hex
    response = client.create_hosted_zone(Name=zone_name, CallerReference=
        reference)
    return parse_zone_id(response['HostedZone']['Id'])