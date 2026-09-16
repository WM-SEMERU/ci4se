def calculate_hash_of_dir(directory, file_list=None):
    md5_hash = md5()
    if not os.path.exists(directory):
        return -1
    try:
        for subdir, dirs, files in os.walk(directory):
            for _file in files:
                file_path = os.path.join(subdir, _file)
                if file_list is not None and file_path not in file_list:
                    continue
                try:
                    _file_object = open(file_path, 'rb')
                except Exception:
                    _file_object.close()
                    return -1
                while 1:
                    buf = _file_object.read(4096)
                    if not buf:
                        break
                    md5_hash.update(md5(buf).hexdigest().encode())
                _file_object.close()
    except Exception:
        return -1
    return md5_hash.hexdigest()