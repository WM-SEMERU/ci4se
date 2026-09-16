def init_config(policy_config):
    global account_id
    exec_options = policy_config.get('execution-options', {})
    for k in ('assume_role', 'profile', 'region', 'dryrun', 'cache'):
        exec_options.pop(k, None)
    if not exec_options.get('output_dir', '').startswith('s3'):
        exec_options['output_dir'] = get_local_output_dir()
    if exec_options.get('account_id'):
        account_id = exec_options['account_id']
    exec_options.update(policy_config['policies'][0].get('mode', {}).get(
        'execution-options', {}))
    if 'assume_role' in exec_options:
        account_id = exec_options['assume_role'].split(':')[4]
    elif account_id is None:
        session = boto3.Session()
        account_id = get_account_id_from_sts(session)
    exec_options['account_id'] = account_id
    if 'metrics_enabled' in exec_options and isinstance(exec_options[
        'metrics_enabled'], bool) and exec_options['metrics_enabled']:
        exec_options['metrics_enabled'] = 'aws'
    return Config.empty(**exec_options)