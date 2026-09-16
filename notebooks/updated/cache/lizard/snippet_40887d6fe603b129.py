def proc_del(self, pid):
    if pid in self._procs:
        del self._procs[pid]
    else:
        log = self._params.get('log', self._discard)
        log.warning('Process %d missing from proc list during deletion', pid)