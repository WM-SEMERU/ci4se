def is_running(self):
    pid = self.get_pid()
    if pid is None:
        return False
    try:
        os.kill(pid, 0)
    except OSError as e:
        if e.errno == errno.ESRCH:
            self.pid_file.release()
            return False
    return True