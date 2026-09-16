def gen_password(password, crypt_salt=None, algorithm='sha512'):
    if not HAS_CRYPT:
        raise CommandExecutionError(
            'gen_password is not available on this operating system because the "crypt" python module is not available.'
            )
    return salt.utils.pycrypto.gen_hash(crypt_salt, password, algorithm)