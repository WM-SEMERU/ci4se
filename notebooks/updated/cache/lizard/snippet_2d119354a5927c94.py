def _get_keyid_by_gpg_key(key_material):
    cmd = 'gpg --with-colons --with-fingerprint'
    ps = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=
        subprocess.PIPE, stdin=subprocess.PIPE)
    out, err = ps.communicate(input=key_material)
    if six.PY3:
        out = out.decode('utf-8')
        err = err.decode('utf-8')
    if 'gpg: no valid OpenPGP data found.' in err:
        raise GPGKeyError('Invalid GPG key material provided')
    return re.search('^fpr:{9}([0-9A-F]{40}):$', out, re.MULTILINE).group(1)