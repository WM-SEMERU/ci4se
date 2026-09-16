def get_base_logfilename(logname):
    logdir = get_base_dir()
    fname = os.path.join(logdir, logname)
    GLOBAL_LOGFILES.append(fname)
    return fname