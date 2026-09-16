def ls(ctx, list_formatted):
    session = create_session(ctx.obj['AWS_PROFILE_NAME'])
    rds = session.client('rds')
    instances = rds.describe_db_instances()
    out = format_output(instances['DBInstances'], list_formatted)
    click.echo('\n'.join(out))