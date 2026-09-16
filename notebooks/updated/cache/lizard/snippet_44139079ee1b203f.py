def get_filepath(filepath):
    if filepath[:7] == 'http://':
        filepath = fuse.http_directory + filepath[6:] + '..'
    if filepath[:8] == 'https://':
        filepath = fuse.https_directory + filepath[7:] + '..'
    print('******** filepath:', filepath)
    return filepath