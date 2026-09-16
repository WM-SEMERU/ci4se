def _get_proc_username(proc):
    try:
        return salt.utils.data.decode(proc.username() if PSUTIL2 else proc.
            username)
    except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
        return None