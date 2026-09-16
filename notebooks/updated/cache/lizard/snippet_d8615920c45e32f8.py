def load_data(handle, reader=None):
    if not reader:
        reader = os.path.splitext(handle)[1][1:].lower()
    if reader not in _READERS:
        raise NeuroMError('Do not have a loader for "%s" extension' % reader)
    filename = _get_file(handle)
    try:
        return _READERS[reader](filename)
    except Exception as e:
        L.exception('Error reading file %s, using "%s" loader', filename,
            reader)
        raise RawDataError('Error reading file %s:\n%s' % (filename, str(e)))