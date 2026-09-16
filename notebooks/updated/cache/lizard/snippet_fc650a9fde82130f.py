def stop_ec2_instance(client, resource):
    instance = EC2Instance.get(resource.id)
    if instance.state in ('stopped', 'terminated'):
        return ActionStatus.IGNORED, {}
    client.stop_instances(InstanceIds=[resource.id])
    return ActionStatus.SUCCEED, {'instance_type': resource.instance_type,
        'public_ip': resource.public_ip}