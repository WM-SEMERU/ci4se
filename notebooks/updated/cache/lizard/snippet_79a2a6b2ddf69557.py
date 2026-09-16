def get_branch():
    proc = Process('git status', ['git', 'status'])
    try:
        while True:
            raw_line = proc.stdout.pop()
            line = raw_line.decode('utf8').strip()
            if line.startswith('On branch '):
                return line[10:]
    finally:
        try:
            proc.join()
        except Exception:
            pass