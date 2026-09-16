def write_monitor_keyring(keyring, monitor_keyring, uid=-1, gid=-1):
    write_file(keyring, monitor_keyring, 384, None, uid, gid)