def files_size(fs0, fs1, files):
    for file_meta in files['deleted_files']:
        file_meta['size'] = fs0.stat(file_meta['path'])['size']
    for file_meta in (files['created_files'] + files['modified_files']):
        file_meta['size'] = fs1.stat(file_meta['path'])['size']
    return files