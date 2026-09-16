def move_tmp_log(logger):
    try:
        logging.shutdown()
        shutil.move(log_tmp_fn, os.path.join(config.data_dir, 'multiqc.log'))
        util_functions.robust_rmtree(log_tmp_dir)
    except (AttributeError, TypeError, IOError):
        pass