def open_file(filename, mode='r', encoding=None, errors='strict', lazy=
    False, atomic=False):
    if lazy:
        return LazyFile(filename, mode, encoding, errors, atomic=atomic)
    f, should_close = open_stream(filename, mode, encoding, errors, atomic=
        atomic)
    if not should_close:
        f = KeepOpenFile(f)
    return f