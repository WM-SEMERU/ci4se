def decrypt_var(source, passphrase=None):
    cmd = [gnupg_bin(), '--decrypt', gnupg_home(), gnupg_verbose(),
        passphrase_file(passphrase)]
    return stderr_with_input(flatten(cmd), source)