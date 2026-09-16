def reader(path):
    p = subprocess.Popen(['7z', 'e', '-so', path], stdout=subprocess.PIPE,
        stderr=file_open(os.devnull, 'w'))
    return io.TextIOWrapper(p.stdout, encoding='utf-8', errors='replace')