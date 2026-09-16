def run(self, parameter_space, kernel_options, tuning_options):
    workflow = self._parameter_sweep(parameter_space, kernel_options, self.
        device_options, tuning_options)
    if tuning_options.verbose:
        with NCDisplay(_error_filter) as display:
            answer = run_parallel_with_display(workflow, self.max_threads,
                display)
    else:
        answer = run_parallel(workflow, self.max_threads)
    if answer is None:
        print('Tuning did not return any results, did an error occur?')
        return None
    result = []
    for chunk in answer:
        result += [d for d in chunk if d['time']]
    return result, {}