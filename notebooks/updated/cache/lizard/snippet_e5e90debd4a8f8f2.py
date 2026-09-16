def gnupg_home():
    if 'GNUPGHOME' in os.environ:
        gnupghome = os.environ['GNUPGHOME']
        if not os.path.isdir(gnupghome):
            raise CryptoritoError('Invalid GNUPGHOME directory')
        return ['--homedir', gnupghome]
    else:
        return []