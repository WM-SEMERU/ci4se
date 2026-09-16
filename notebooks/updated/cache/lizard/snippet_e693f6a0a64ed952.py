def _patch_file(path, content):
    f = open(path)
    existing_content = f.read()
    f.close()
    if existing_content == content:
        log.warn('Already patched.')
        return False
    log.warn('Patching...')
    _rename_path(path)
    f = open(path, 'w')
    try:
        f.write(content)
    finally:
        f.close()
    return True