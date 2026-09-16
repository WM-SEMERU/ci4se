def close_process_handles(self):
    for pid in self.get_process_ids():
        aProcess = self.get_process(pid)
        try:
            aProcess.close_handle()
        except Exception:
            e = sys.exc_info()[1]
            try:
                msg = 'Cannot close process handle %s, reason: %s'
                msg %= aProcess.hProcess.value, str(e)
                warnings.warn(msg)
            except Exception:
                pass