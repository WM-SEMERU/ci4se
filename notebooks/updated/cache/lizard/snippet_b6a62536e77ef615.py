def get_unique_file_path_suffix(file_path, separator='-', i=0):
    basename = os.path.splitext(file_path)
    if i != 0:
        file_path_test = os.path.join('%s%s%s%s' % (basename[0], separator,
            i, basename[1]))
    else:
        file_path_test = file_path
    if os.path.isfile(file_path_test):
        return OsmDownloaderDialog.get_unique_file_path_suffix(file_path,
            separator, i + 1)
    else:
        return i