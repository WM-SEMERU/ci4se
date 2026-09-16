def is_running(pid):
    process = get_process(pid)
    if process and process.is_running() and process.status() != 'zombie':
        return True
    else:
        return False