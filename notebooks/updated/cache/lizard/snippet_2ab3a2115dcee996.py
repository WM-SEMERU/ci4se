def _read_execute_info(path, parents):
    path = os.path.join(path, 'StarCraft II/ExecuteInfo.txt')
    if os.path.exists(path):
        with open(path, 'rb') as f:
            for line in f:
                parts = [p.strip() for p in line.decode('utf-8').split('=')]
                if len(parts) == 2 and parts[0] == 'executable':
                    exec_path = parts[1].replace('\\', '/')
                    for _ in range(parents):
                        exec_path = os.path.dirname(exec_path)
                    return exec_path