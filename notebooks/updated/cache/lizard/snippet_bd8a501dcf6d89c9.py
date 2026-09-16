def ls(ctx, name, list_instances):
    session = create_session(ctx.obj['AWS_PROFILE_NAME'])
    client = session.client('elb')
    inst = {'LoadBalancerDescriptions': []}
    if name == '*':
        inst = client.describe_load_balancers()
    else:
        try:
            inst = client.describe_load_balancers(LoadBalancerNames=[name])
        except ClientError as e:
            click.echo(e, err=True)
    for i in inst['LoadBalancerDescriptions']:
        click.echo(i['LoadBalancerName'])
        if list_instances:
            for ec2 in i['Instances']:
                health = client.describe_instance_health(LoadBalancerName=
                    name, Instances=[ec2])
                click.echo('{0}\t{1}'.format(ec2['InstanceId'], health[
                    'InstanceStates'][0]['State']))