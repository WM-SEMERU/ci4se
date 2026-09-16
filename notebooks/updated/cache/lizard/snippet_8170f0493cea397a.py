def is_rpm(path):
    import magic
    m = magic.open(magic.MAGIC_MIME)
    m.load()
    mime = m.file(path)
    if 'rpm' in mime or 'directory' in mime:
        return True
    else:
        juicer.utils.Log.log_info('error: File `%s` is not an rpm' % path)
        return False