def deploy_lambda(awsclient, function_name, role, handler_filename,
    handler_function, folders, description, timeout, memory, subnet_ids=
    None, security_groups=None, artifact_bucket=None, zipfile=None,
    fail_deployment_on_unsuccessful_ping=False, runtime='python2.7',
    settings=None, environment=None, retention_in_days=None):
    if lambda_exists(awsclient, function_name):
        function_version = _update_lambda(awsclient, function_name,
            handler_filename, handler_function, folders, role, description,
            timeout, memory, subnet_ids, security_groups, artifact_bucket=
            artifact_bucket, zipfile=zipfile, environment=environment)
    else:
        if not zipfile:
            return 1
        log.info('buffer size: %0.2f MB' % float(len(zipfile) / 1000000.0))
        function_version = _create_lambda(awsclient, function_name, role,
            handler_filename, handler_function, folders, description,
            timeout, memory, subnet_ids, security_groups, artifact_bucket,
            zipfile, runtime=runtime, environment=environment)
    if retention_in_days:
        log_group_name = '/aws/lambda/%s' % function_name
        put_retention_policy(awsclient, log_group_name, retention_in_days)
    pong = ping(awsclient, function_name, version=function_version)
    if 'alive' in str(pong):
        log.info(colored.green("Great you're already accepting a ping " +
            'in your Lambda function'))
    elif fail_deployment_on_unsuccessful_ping and not 'alive' in pong:
        log.info(colored.red('Pinging your lambda function failed'))
        return 1
    else:
        log.info(colored.red('Please consider adding a reaction to a ' +
            'ping event to your lambda function'))
    _deploy_alias(awsclient, function_name, function_version)
    return 0