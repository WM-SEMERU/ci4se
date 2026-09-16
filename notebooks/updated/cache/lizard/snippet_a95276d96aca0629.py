def start_raylet_monitor(redis_address, stdout_file=None, stderr_file=None,
    redis_password=None, config=None):
    gcs_ip_address, gcs_port = redis_address.split(':')
    redis_password = redis_password or ''
    config = config or {}
    config_str = ','.join(['{},{}'.format(*kv) for kv in config.items()])
    command = [RAYLET_MONITOR_EXECUTABLE, '--redis_address={}'.format(
        gcs_ip_address), '--redis_port={}'.format(gcs_port),
        '--config_list={}'.format(config_str)]
    if redis_password:
        command += [redis_password]
    process_info = start_ray_process(command, ray_constants.
        PROCESS_TYPE_RAYLET_MONITOR, stdout_file=stdout_file, stderr_file=
        stderr_file)
    return process_info