def is_process_running(process_name):
    is_running = False
    if os.path.isfile('/usr/bin/pgrep'):
        dev_null = open(os.devnull, 'wb')
        returncode = subprocess.call(['/usr/bin/pgrep', process_name],
            stdout=dev_null)
        is_running = bool(returncode == 0)
    return is_running