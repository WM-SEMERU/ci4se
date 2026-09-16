def create_mon_path(path, uid=-1, gid=-1):
    if not os.path.exists(path):
        os.makedirs(path)
        os.chown(path, uid, gid)