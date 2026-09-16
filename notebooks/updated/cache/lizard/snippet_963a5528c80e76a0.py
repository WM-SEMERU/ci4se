def set_logfile(path, instance):
    global logfile
    logfile = os.path.normpath(path) + '/hfos.' + instance + '.log'