def import_private_key_from_file(filename, passphrase=None):
    with open(filename, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(),
            password=passphrase, backend=default_backend())
    return private_key