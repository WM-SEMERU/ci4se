def get_key_auth_cb(key_filepath):

    def auth_cb(ssh):
        key = ssh_pki_import_privkey_file(key_filepath)
        ssh.userauth_publickey(key)
    return auth_cb