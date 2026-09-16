def new(name, bucket, timeout, memory, description, subnet_ids,
    security_group_ids):
    config = {}
    if timeout:
        config['timeout'] = timeout
    if memory:
        config['memory'] = memory
    if description:
        config['description'] = description
    if subnet_ids:
        config['subnet_ids'] = subnet_ids
    if security_group_ids:
        config['security_group_ids'] = security_group_ids
    lambder.create_project(name, bucket, config)