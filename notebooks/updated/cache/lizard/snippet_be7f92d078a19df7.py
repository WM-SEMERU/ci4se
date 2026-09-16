def set_kill_on_exit_mode(bKillOnExit=False):
    try:
        win32.DebugSetProcessKillOnExit(bKillOnExit)
    except (AttributeError, WindowsError):
        return False
    return True