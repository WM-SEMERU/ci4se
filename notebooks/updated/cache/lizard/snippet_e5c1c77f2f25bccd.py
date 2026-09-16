def verify_fft_options(opt, parser):
    if opt.fftw_measure_level not in [0, 1, 2, 3]:
        parser.error('{0} is not a valid FFTW measure level.'.format(opt.
            fftw_measure_level))
    if opt.fftw_import_system_wisdom and (opt.fftw_input_float_wisdom_file
         is not None or opt.fftw_input_double_wisdom_file is not None):
        parser.error(
            'If --fftw-import-system-wisdom is given, then you cannot give either of --fftw-input-float-wisdom-file or --fftw-input-double-wisdom-file'
            )
    if opt.fftw_threads_backend is not None:
        if opt.fftw_threads_backend not in ['openmp', 'pthreads', 'unthreaded'
            ]:
            parser.error(
                "Invalid threads backend; must be 'openmp', 'pthreads' or 'unthreaded'"
                )