def mark_process_dead(pid, path=None):
    if path is None:
        path = os.environ.get('prometheus_multiproc_dir')
    for f in glob.glob(os.path.join(path, 'gauge_livesum_{0}.db'.format(pid))):
        os.remove(f)
    for f in glob.glob(os.path.join(path, 'gauge_liveall_{0}.db'.format(pid))):
        os.remove(f)