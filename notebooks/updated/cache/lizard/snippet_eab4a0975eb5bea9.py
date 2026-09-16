def _detach_process():
    pid = os.fork()
    if pid > 0:
        os.waitpid(pid, 0)
        return True
    os.setsid()
    pid = os.fork()
    if pid > 0:
        os._exit(os.EX_OK)
    return False