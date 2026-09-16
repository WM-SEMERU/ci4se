def list_files(x, path=''):
    logger_directory.info('enter list_files')
    file_list = []
    if path:
        files = os.listdir(path)
        for file in files:
            if file.endswith(x) and not file.startswith(('$', '~', '.')):
                file_list.append(os.path.join(path, file))
    else:
        files = os.listdir()
        for file in files:
            if file.endswith(x) and not file.startswith(('$', '~', '.')):
                file_list.append(file)
    logger_directory.info('exit list_files')
    return file_list