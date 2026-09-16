def rnaseq_prep_samples(config, run_info_yaml, parallel, dirs, samples):
    pipeline = dd.get_in_samples(samples, dd.get_analysis)
    trim_reads_set = any([tz.get_in(['algorithm', 'trim_reads'], d) for d in
        dd.sample_data_iterator(samples)])
    resources = ['picard']
    needs_trimming = _is_smallrnaseq(pipeline) or trim_reads_set
    if needs_trimming:
        resources.append('atropos')
    with prun.start(_wres(parallel, resources), samples, config, dirs,
        'trimming', max_multicore=1 if not needs_trimming else None
        ) as run_parallel:
        with profile.report('organize samples', dirs):
            samples = run_parallel('organize_samples', [[dirs, config,
                run_info_yaml, [x[0]['description'] for x in samples]]])
            samples = run_parallel('prepare_sample', samples)
        if needs_trimming:
            with profile.report('adapter trimming', dirs):
                if _is_smallrnaseq(pipeline):
                    samples = run_parallel('trim_srna_sample', samples)
                else:
                    samples = run_parallel('trim_sample', samples)
    return samples