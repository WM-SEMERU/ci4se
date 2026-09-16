def local_run():
    server_software = os.environ.get('SERVER_SOFTWARE')
    if server_software is None:
        return True
    if 'remote_api' in server_software:
        return False
    if server_software.startswith(('Development', 'testutil')):
        return True
    return False