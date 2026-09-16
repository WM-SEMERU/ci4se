def enc_file(name, out=None, **kwargs):
    try:
        data = __salt__['cp.get_file_str'](name)
    except Exception as e:
        with salt.utils.files.fopen(name, 'rb') as f:
            data = salt.utils.stringutils.to_unicode(f.read())
    d = enc(data, **kwargs)
    if out:
        if os.path.isfile(out):
            raise Exception('file:{0} already exist.'.format(out))
        with salt.utils.files.fopen(out, 'wb') as f:
            f.write(salt.utils.stringutils.to_bytes(d))
        return 'Wrote: {0}'.format(out)
    return d