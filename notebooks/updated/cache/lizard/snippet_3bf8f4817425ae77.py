def end_logging(filename=None):
    if logutil.global_logging_started:
        if filename:
            print('Trailer file written to: ', filename)
        else:
            print('No trailer file saved...')
        logutil.teardown_global_logging()
    else:
        print('No trailer file saved...')