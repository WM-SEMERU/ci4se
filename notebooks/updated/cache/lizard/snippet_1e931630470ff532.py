def call_sockeye_average(model_dir: str, log_fname: str):
    params_best_fname = os.path.join(model_dir, C.PARAMS_BEST_NAME)
    params_best_single_fname = os.path.join(model_dir, PARAMS_BEST_SINGLE)
    params_average_fname = os.path.join(model_dir, PARAMS_AVERAGE)
    command = [sys.executable, '-m', 'sockeye.average', '--metric={}'.
        format(AVERAGE_METRIC), '-n', str(AVERAGE_NUM_CHECKPOINTS),
        '--output={}'.format(params_average_fname), '--strategy={}'.format(
        AVERAGE_STRATEGY), model_dir]
    command_fname = os.path.join(model_dir, FILE_COMMAND.format(
        'sockeye.average'))
    if not os.path.exists(command_fname):
        os.symlink(os.path.basename(os.path.realpath(params_best_fname)),
            params_best_single_fname)
        os.remove(params_best_fname)
        with open(log_fname, 'wb') as log:
            logging.info('sockeye.average: %s', os.path.join(model_dir,
                params_best_fname))
            logging.info('Log: %s', log_fname)
            subprocess.check_call(command, stderr=log)
        os.symlink(PARAMS_AVERAGE, params_best_fname)
        logging.info('Command: %s', command_fname)
        print_command(command, command_fname)