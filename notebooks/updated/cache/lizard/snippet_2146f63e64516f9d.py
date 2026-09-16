def detach(self, dwProcessId, bIgnoreExceptions=False):
    try:
        aProcess = self.system.get_process(dwProcessId)
    except KeyError:
        aProcess = Process(dwProcessId)
    try:
        win32.DebugActiveProcessStop
        can_detach = True
    except AttributeError:
        can_detach = False
    try:
        if can_detach and self.lastEvent and self.lastEvent.get_pid(
            ) == dwProcessId:
            self.cont(self.lastEvent)
    except Exception:
        if not bIgnoreExceptions:
            raise
        e = sys.exc_info()[1]
        warnings.warn(str(e), RuntimeWarning)
    self.__cleanup_process(dwProcessId, bIgnoreExceptions=bIgnoreExceptions)
    try:
        if can_detach:
            try:
                win32.DebugActiveProcessStop(dwProcessId)
            except Exception:
                if not bIgnoreExceptions:
                    raise
                e = sys.exc_info()[1]
                warnings.warn(str(e), RuntimeWarning)
        else:
            try:
                aProcess.kill()
            except Exception:
                if not bIgnoreExceptions:
                    raise
                e = sys.exc_info()[1]
                warnings.warn(str(e), RuntimeWarning)
    finally:
        aProcess.clear()