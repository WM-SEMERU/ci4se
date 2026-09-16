def teardown_coverage(config, kernel, output_loc=None):
    language = kernel.language
    if language.startswith('python'):
        msg_id = kernel.kc.execute(_python_teardown)
        kernel.await_idle(msg_id, 60)
        cov = get_cov(config)
        _merge_nbval_coverage_data(cov)
    else:
        pass