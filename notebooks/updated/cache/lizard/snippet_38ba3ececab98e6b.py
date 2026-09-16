def handle_termination(cls, pid, is_cancel=True):
    try:
        main_proc = psutil.Process(pid=pid)
        child_procs = main_proc.children(recursive=True)
        for child_proc in child_procs:
            try:
                os.kill(child_proc.pid, signal.SIGKILL)
            except (TypeError, OSError):
                pass
        os.kill(main_proc.pid, signal.SIGKILL)
    except (TypeError, psutil.Error, OSError):
        try:
            os.kill(pid, signal.SIGKILL)
        except OSError:
            pass