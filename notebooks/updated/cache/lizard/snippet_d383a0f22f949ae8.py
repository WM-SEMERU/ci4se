def write_path(path, s, owner=None, group=None, mode=None, utimes=None,
    sync=False):
    path = os.path.abspath(path)
    fd, tmp_path = tempfile.mkstemp(suffix='.tmp', prefix=
        '.ansible_mitogen_transfer-', dir=os.path.dirname(path))
    fp = os.fdopen(fd, 'wb', mitogen.core.CHUNK_SIZE)
    LOG.debug('write_path(path=%r) temporary file: %s', path, tmp_path)
    try:
        try:
            if mode:
                set_file_mode(tmp_path, mode, fd=fp.fileno())
            if owner or group:
                set_file_owner(tmp_path, owner, group, fd=fp.fileno())
            fp.write(s)
        finally:
            fp.close()
        if sync:
            os.fsync(fp.fileno())
        os.rename(tmp_path, path)
    except BaseException:
        os.unlink(tmp_path)
        raise
    if utimes:
        os.utime(path, utimes)