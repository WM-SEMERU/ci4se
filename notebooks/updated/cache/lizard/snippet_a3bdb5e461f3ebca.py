def write_keyring(path, key, uid=-1, gid=-1):
    tmp_file = tempfile.NamedTemporaryFile('wb', delete=False)
    tmp_file.write(key)
    tmp_file.close()
    keyring_dir = os.path.dirname(path)
    if not path_exists(keyring_dir):
        makedir(keyring_dir, uid, gid)
    shutil.move(tmp_file.name, path)