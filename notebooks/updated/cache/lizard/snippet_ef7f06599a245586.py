def clean_pid_file(pidfile):
    if pidfile and os.path.exists(pidfile):
        os.unlink(pidfile)