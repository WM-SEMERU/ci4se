def kill_all():
    for i in dispatchers.all_instances():
        try:
            os.kill(-i.pid, signal.SIGKILL)
        except OSError:
            pass