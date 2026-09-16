def get_private_key(key_path, password_path=None):
    assert key_path, key_path
    if not os.path.exists(key_path):
        log.fatal('%s: no such file', key_path)
        return None
    if not check_permission_safety(key_path):
        log.fatal('Private key file %s must be readable only by its owner.',
            key_path)
        return None
    if password_path and not check_permission_safety(password_path):
        log.fatal('Password file %s must be readable only by its owner.',
            password_path)
        return None
    with open(key_path) as keyfile:
        private_key = keyfile.readline().strip()
        if is_hex(private_key) and len(decode_hex(private_key)) == 32:
            log.warning(
                'Private key in raw format. Consider switching to JSON-encoded'
                )
        else:
            keyfile.seek(0)
            try:
                json_data = json.load(keyfile)
                if password_path:
                    with open(password_path) as password_file:
                        password = password_file.readline().strip()
                else:
                    password = getpass.getpass(
                        'Enter the private key password: ')
                if json_data['crypto']['kdf'] == 'pbkdf2':
                    password = password.encode()
                private_key = encode_hex(decode_keyfile_json(json_data,
                    password))
            except ValueError:
                log.fatal('Invalid private key format or password!')
                return None
    return private_key