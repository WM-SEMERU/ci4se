def get_tempdir():
    tempdir = os.path.join(tempfile.gettempdir(), 'pyelastix')
    if not os.path.isdir(tempdir):
        os.makedirs(tempdir)
    for fname in os.listdir(tempdir):
        dirName = os.path.join(tempdir, fname)
        if not (os.path.isdir(dirName) and fname.startswith('id_')):
            continue
        try:
            pid = int(fname.split('_')[1])
        except Exception:
            continue
        if not _is_pid_running(pid):
            _clear_dir(dirName)
    tid = id(threading.current_thread() if hasattr(threading,
        'current_thread') else threading.currentThread())
    dir = os.path.join(tempdir, 'id_%i_%i' % (os.getpid(), tid))
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return dir