def detect_hooks():
    flog.debug('Detecting hooks ...')
    present = any([hasattr(hook, 'RENAMER') for hook in sys.meta_path])
    if present:
        flog.debug('Detected.')
    else:
        flog.debug('Not detected.')
    return present