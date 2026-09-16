def add_site_dir(dir_name, before=None, _path=None):
    log.log(5, 'add_site_dir(%r, before=%r)', dir_name, before)
    if not os.path.exists(dir_name):
        return
    path = _path or SysPathInserter(index=before)
    path.add(dir_name)
    for file_name in os.listdir(dir_name):
        if file_name.startswith('.'):
            continue
        if file_name.endswith('.pth'):
            _process_pth(path, dir_name, file_name)
        if os.path.exists(os.path.join(dir_name, file_name, '__site__.pth')):
            _process_pth(path, os.path.join(dir_name, file_name),
                '__site__.pth')