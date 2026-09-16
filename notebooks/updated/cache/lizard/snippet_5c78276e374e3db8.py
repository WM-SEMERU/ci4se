def reload(self):
    pid = self._read_pidfile()
    if pid is None or pid != os.getpid():
        raise DaemonError(
            'Daemon.reload() should only be called by the daemon process itself'
            )
    new_environ = os.environ.copy()
    new_environ['DAEMONOCLE_RELOAD'] = 'true'
    subprocess.call([sys.executable] + sys.argv, cwd=self._orig_workdir,
        env=new_environ)
    self._shutdown('Shutting down for reload')