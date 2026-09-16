def getVolInfo(*paths):
    path = os.path.join(*paths)
    path = os.path.expanduser(path)
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    return {'free': free, 'used': total - free, 'total': total}