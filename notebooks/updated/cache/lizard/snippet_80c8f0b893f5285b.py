def atomic_write(filename, content, overwrite=True, permissions=420,
    encoding='utf-8'):
    filename = os.path.expanduser(filename)
    if not overwrite and os.path.exists(filename):
        raise WriteError('file already exists: {0}'.format(filename))
    dirname = os.path.dirname(filename)
    with tf.NamedTemporaryFile(dir=dirname, prefix='.', delete=False) as tmp:
        if isinstance(content, six.string_types):
            tmp.write(content.decode(encoding))
        else:
            tmp.write(content)
    os.chmod(tmp.name, permissions)
    os.rename(tmp.name, filename)