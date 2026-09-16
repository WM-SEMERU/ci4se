def _import(self, record_key, record_data, overwrite=True, last_modified=
    0.0, **kwargs):
    file_path = os.path.join(self.collection_folder, record_key)
    from os import path, makedirs
    if not overwrite:
        if path.exists(file_path):
            return False
    file_root, file_name = path.split(file_path)
    if file_root:
        if not path.exists(file_root):
            makedirs(file_root)
    with open(file_path, 'wb') as f:
        f.write(record_data)
        f.close()
    import re
    if re.search('\\.drep$', file_name):
        from os import utime
        file_time = 1
        utime(file_path, times=(file_time, file_time))
    elif last_modified:
        from os import utime
        utime(file_path, times=(last_modified, last_modified))
    return True