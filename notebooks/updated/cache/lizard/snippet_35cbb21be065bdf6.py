def start_monitor(redis_address, stdout_file=None, stderr_file=None,
    autoscaling_config=None, redis_password=None):
    monitor_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'monitor.py')
    command = [sys.executable, '-u', monitor_path, '--redis-address=' + str
        (redis_address)]
    if autoscaling_config:
        command.append('--autoscaling-config=' + str(autoscaling_config))
    if redis_password:
        command.append('--redis-password=' + redis_password)
    process_info = start_ray_process(command, ray_constants.
        PROCESS_TYPE_MONITOR, stdout_file=stdout_file, stderr_file=stderr_file)
    return process_info