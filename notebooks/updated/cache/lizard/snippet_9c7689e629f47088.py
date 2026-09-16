def stop(self):
    if self.pidfile is None:
        raise DaemonError('Cannot stop daemon without PID file')
    pid = self._read_pidfile()
    if pid is None:
        self._emit_warning('{prog} is not running'.format(prog=self.prog))
        return
    self._emit_message('Stopping {prog} ... '.format(prog=self.prog))
    try:
        os.kill(pid, signal.SIGTERM)
    except OSError as ex:
        self._emit_failed()
        self._emit_error(str(ex))
        sys.exit(1)
    if self._pid_is_alive(pid, timeout=self.stop_timeout):
        self._emit_failed()
        self._emit_error(
            'Timed out while waiting for process (PID {pid}) to terminate'.
            format(pid=pid))
        sys.exit(1)
    self._emit_ok()