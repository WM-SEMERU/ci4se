def _evaluate_model_single_file(target_folder, test_file):
    logging.info('Create running model...')
    model_src = get_latest_model(target_folder, 'model')
    model_file_pointer = tempfile.NamedTemporaryFile(delete=False)
    model_use = model_file_pointer.name
    model_file_pointer.close()
    logging.info('Adjusted model is in %s.', model_use)
    create_adjusted_model_for_percentages(model_src, model_use)
    project_root = get_project_root()
    time_prefix = time.strftime('%Y-%m-%d-%H-%M')
    logging.info("Evaluate '%s' with '%s'...", model_src, test_file)
    logfilefolder = os.path.join(project_root, 'logs/')
    if not os.path.exists(logfilefolder):
        os.makedirs(logfilefolder)
    logfile = os.path.join(project_root, 'logs/%s-error-evaluation.log' %
        time_prefix)
    with open(logfile, 'w') as log, open(model_use, 'r') as modl_src_p:
        p = subprocess.Popen([get_nntoolkit(), 'run', '--batch-size', '1',
            '-f%0.4f', test_file], stdin=modl_src_p, stdout=log)
        ret = p.wait()
        if ret != 0:
            logging.error('nntoolkit finished with ret code %s', str(ret))
            sys.exit()
    return logfile, model_use