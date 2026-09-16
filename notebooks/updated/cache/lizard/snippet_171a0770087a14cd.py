def peakcall_prepare(data, run_parallel):
    caller_fns = get_callers()
    to_process = []
    for sample in data:
        mimic = copy.copy(sample[0])
        callers = dd.get_peakcaller(sample[0])
        if not isinstance(callers, list):
            callers = [callers]
        for caller in callers:
            if caller in caller_fns:
                mimic['peak_fn'] = caller
                name = dd.get_sample_name(mimic)
                mimic = _check(mimic, data)
                if mimic:
                    to_process.append(mimic)
                else:
                    logger.info(
                        'Skipping peak calling. No input sample for %s' % name)
    if to_process:
        after_process = run_parallel('peakcalling', to_process)
        data = _sync(data, after_process)
    return data