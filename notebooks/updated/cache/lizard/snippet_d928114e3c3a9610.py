def tune(runner, kernel_options, device_options, tuning_options):
    tune_params = tuning_options.tune_params
    restrictions = tuning_options.restrictions
    verbose = tuning_options.verbose
    parameter_space = itertools.product(*tune_params.values())
    if restrictions is not None:
        parameter_space = filter(lambda p: util.check_restrictions(
            restrictions, p, tune_params.keys(), verbose), parameter_space)
    results, env = runner.run(parameter_space, kernel_options, tuning_options)
    return results, env