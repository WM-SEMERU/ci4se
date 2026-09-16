def track_from_filename(filename, filetype=None, timeout=
    DEFAULT_ASYNC_TIMEOUT, force_upload=False):
    filetype = filetype or filename.split('.')[-1]
    file_object = open(filename, 'rb')
    result = track_from_file(file_object, filetype, timeout, force_upload)
    file_object.close()
    return result