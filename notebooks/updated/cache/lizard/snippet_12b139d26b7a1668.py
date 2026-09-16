def _request_one_trial_job(self):
    if not self.generated_hyper_configs:
        ret = {'parameter_id': '-1_0_0', 'parameter_source': 'algorithm',
            'parameters': ''}
        send(CommandType.NoMoreTrialJobs, json_tricks.dumps(ret))
        return
    assert self.generated_hyper_configs
    params = self.generated_hyper_configs.pop()
    ret = {'parameter_id': params[0], 'parameter_source': 'algorithm',
        'parameters': params[1]}
    self.parameters[params[0]] = params[1]
    send(CommandType.NewTrialJob, json_tricks.dumps(ret))
    self.credit -= 1