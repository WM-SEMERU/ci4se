def get_process_pids(self, process):
    pids = []
    cmd_line_glob = '/proc/[0-9]*/cmdline'
    cmd_line_paths = glob.glob(cmd_line_glob)
    for path in cmd_line_paths:
        try:
            with open(path, 'r') as f:
                cmd_line = f.read().strip()
                if process in cmd_line:
                    pids.append(path.split('/')[2])
        except IOError as e:
            continue
    return pids