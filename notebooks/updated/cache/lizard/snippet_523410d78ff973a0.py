def ssh_config(ssh_user, ssh_private_key_file):
    try:
        ssh_file = NamedTemporaryFile(delete=False, mode='w+')
        ssh_file.write('Host *\n')
        ssh_file.write('    IdentityFile %s\n' % ssh_private_key_file)
        ssh_file.write('    User %s' % ssh_user)
        ssh_file.close()
        yield ssh_file.name
    finally:
        with ignored(OSError):
            os.remove(ssh_file.name)