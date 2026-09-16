def create_ecs_service_role(provider, context, **kwargs):
    role_name = kwargs.get('role_name', 'ecsServiceRole')
    client = get_session(provider.region).client('iam')
    try:
        client.create_role(RoleName=role_name, AssumeRolePolicyDocument=
            get_ecs_assumerole_policy().to_json())
    except ClientError as e:
        if 'already exists' in str(e):
            pass
        else:
            raise
    policy = Policy(Statement=[Statement(Effect=Allow, Resource=['*'],
        Action=[ecs.CreateCluster, ecs.DeregisterContainerInstance, ecs.
        DiscoverPollEndpoint, ecs.Poll, ecs.Action('Submit*')])])
    client.put_role_policy(RoleName=role_name, PolicyName=
        'AmazonEC2ContainerServiceRolePolicy', PolicyDocument=policy.to_json())
    return True