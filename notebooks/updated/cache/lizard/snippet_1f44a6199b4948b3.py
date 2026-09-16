def _list_result_paths(target_path, log_file_name='log'):
    result_list = []
    for root, _dirs, _files in os.walk(os.path.abspath(target_path)):
        for name in _files:
            if name == log_file_name:
                result_list.append(root)
    return result_list