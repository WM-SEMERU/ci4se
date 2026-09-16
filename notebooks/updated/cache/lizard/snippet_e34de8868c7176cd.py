def _get_user_processes():
    uid = os.getuid()
    for proc in psutil.process_iter():
        try:
            if proc.uids.real == uid:
                yield proc, proc.exe
        except psutil.AccessDenied:
            try:
                path = common.which(proc.name)
                if not path and common.IS_MACOSX:
                    cwd = _get_process_cwd(proc.pid)
                    if not cwd:
                        continue
                    path = os.path.join(cwd, proc.cmdline[0])
                yield proc, path
            except (psutil.AccessDenied, OSError):
                pass
        except psutil.NoSuchProcess:
            pass