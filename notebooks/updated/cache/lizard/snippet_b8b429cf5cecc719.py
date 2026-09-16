def handle_report_metric_data(self, data):
    logger.debug('handle report metric data = %s', data)
    assert 'value' in data
    value = extract_scalar_reward(data['value'])
    if self.optimize_mode is OptimizeMode.Maximize:
        reward = -value
    else:
        reward = value
    assert 'parameter_id' in data
    s, i, _ = data['parameter_id'].split('_')
    logger.debug('bracket id = %s, metrics value = %s, type = %s', s, value,
        data['type'])
    s = int(s)
    assert 'type' in data
    if data['type'] == 'FINAL':
        assert 'sequence' in data
        self.brackets[s].set_config_perf(int(i), data['parameter_id'], sys.
            maxsize, value)
        self.completed_hyper_configs.append(data)
        _parameters = self.parameters[data['parameter_id']]
        _parameters.pop(_KEY)
        self.cg.new_result(loss=reward, budget=data['sequence'], parameters
            =_parameters, update_model=True)
    elif data['type'] == 'PERIODICAL':
        self.brackets[s].set_config_perf(int(i), data['parameter_id'], data
            ['sequence'], value)
    else:
        raise ValueError('Data type not supported: {}'.format(data['type']))