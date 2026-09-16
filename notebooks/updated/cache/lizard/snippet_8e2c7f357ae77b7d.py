def _shutdown_minions(self):
    setproctitle('pyres_manager: Waiting on children to shutdown.')
    for minion in self._workers.values():
        minion.terminate()
        minion.join()