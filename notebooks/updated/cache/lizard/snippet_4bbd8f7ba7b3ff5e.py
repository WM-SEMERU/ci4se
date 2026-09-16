def report_intermediate_result(metric):
    global _intermediate_seq
    assert _params is not None, 'nni.get_next_parameter() needs to be called before report_intermediate_result'
    metric = json_tricks.dumps({'parameter_id': _params['parameter_id'],
        'trial_job_id': trial_env_vars.NNI_TRIAL_JOB_ID, 'type':
        'PERIODICAL', 'sequence': _intermediate_seq, 'value': metric})
    _intermediate_seq += 1
    platform.send_metric(metric)