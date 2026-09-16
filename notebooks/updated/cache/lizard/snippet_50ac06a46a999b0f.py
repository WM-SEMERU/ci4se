def clean_proc_dir(opts):
    for basefilename in os.listdir(salt.minion.get_proc_dir(opts['cachedir'])):
        fn_ = os.path.join(salt.minion.get_proc_dir(opts['cachedir']),
            basefilename)
        with salt.utils.files.fopen(fn_, 'rb') as fp_:
            job = None
            try:
                job = salt.payload.Serial(opts).load(fp_)
            except Exception:
                if salt.utils.platform.is_windows():
                    fp_.close()
                try:
                    os.unlink(fn_)
                    continue
                except OSError:
                    continue
            log.debug(
                'schedule.clean_proc_dir: checking job %s for process existence'
                , job)
            if job is not None and 'pid' in job:
                if salt.utils.process.os_is_running(job['pid']):
                    log.debug(
                        'schedule.clean_proc_dir: Cleaning proc dir, pid %s still exists.'
                        , job['pid'])
                else:
                    if salt.utils.platform.is_windows():
                        fp_.close()
                    try:
                        os.unlink(fn_)
                    except OSError:
                        pass