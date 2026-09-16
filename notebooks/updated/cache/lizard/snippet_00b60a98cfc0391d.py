def watchdog_pid():
    result = sh('netstat -tulpn 2>/dev/null | grep 127.0.0.1:{:d}'.format(
        SPHINX_AUTOBUILD_PORT), capture=True, ignore_error=True)
    pid = result.strip()
    pid = pid.split()[-1] if pid else None
    pid = pid.split('/', 1)[0] if pid and pid != '-' else None
    return pid