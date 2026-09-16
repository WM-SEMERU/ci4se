def generate_multiple_parameters(self, parameter_id_list):
    result = []
    for parameter_id in parameter_id_list:
        try:
            _logger.debug('generating param for {}'.format(parameter_id))
            res = self.generate_parameters(parameter_id)
        except nni.NoMoreTrialError:
            return result
        result.append(res)
    return result