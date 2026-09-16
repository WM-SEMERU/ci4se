def _aws_get_instance_by_tag(region, name, tag, raw):
    client = boto3.session.Session().client('ec2', region)
    matching_reservations = client.describe_instances(Filters=[{'Name': tag,
        'Values': [name]}]).get('Reservations', [])
    instances = []
    [[instances.append(_aws_instance_from_dict(region, instance, raw)) for
        instance in reservation.get('Instances')] for reservation in
        matching_reservations if reservation]
    return instances