def getcwd(fs_encoding=FS_ENCODING, cwd_fnc=os.getcwd):
    path = fsdecode(cwd_fnc(), fs_encoding=fs_encoding)
    return os.path.abspath(path)