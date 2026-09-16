def compile_output(self, input_sample, num_samples, num_params,
    maximum_combo, num_groups=None):
    if num_groups is None:
        num_groups = num_params
    self.check_input_sample(input_sample, num_groups, num_samples)
    index_list = self._make_index_list(num_samples, num_params, num_groups)
    output = np.zeros((np.size(maximum_combo) * (num_groups + 1), num_params))
    for counter, combo in enumerate(maximum_combo):
        output[index_list[counter]] = np.array(input_sample[index_list[combo]])
    return output