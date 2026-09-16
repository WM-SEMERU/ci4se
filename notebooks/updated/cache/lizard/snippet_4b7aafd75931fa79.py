def update_experiment():
    experiment_config = Experiments()
    experiment_dict = experiment_config.get_all_experiments()
    if not experiment_dict:
        return None
    for key in experiment_dict.keys():
        if isinstance(experiment_dict[key], dict):
            if experiment_dict[key].get('status') != 'STOPPED':
                nni_config = Config(experiment_dict[key]['fileName'])
                rest_pid = nni_config.get_config('restServerPid')
                if not detect_process(rest_pid):
                    experiment_config.update_experiment(key, 'status',
                        'STOPPED')
                    continue
                rest_port = nni_config.get_config('restServerPort')
                startTime, endTime = get_experiment_time(rest_port)
                if startTime:
                    experiment_config.update_experiment(key, 'startTime',
                        startTime)
                if endTime:
                    experiment_config.update_experiment(key, 'endTime', endTime
                        )
                status = get_experiment_status(rest_port)
                if status:
                    experiment_config.update_experiment(key, 'status', status)