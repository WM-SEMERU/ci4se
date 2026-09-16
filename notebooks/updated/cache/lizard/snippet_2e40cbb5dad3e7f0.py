def _clean_prior(self):
    if self._loaded:
        try:
            pid_file = daemon.get_daemon_pidfile(self)
            if os.path.isfile(pid_file):
                pid = int(common.readfile(pid_file))
                if pid and not daemon.pid_exists(pid):
                    common.safe_remove_file(pid_file)
                    raise ValueError
        except (ValueError, TypeError):
            self._clean()
            return True
    return False