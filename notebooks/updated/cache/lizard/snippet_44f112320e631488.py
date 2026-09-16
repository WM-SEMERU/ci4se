def find_binary(self, binary):
    if os.path.exists(binary):
        return binary
    binary_name = os.path.basename(binary)
    search_paths = os.environ['PATH'].split(':')
    default_paths = ['/usr/bin', '/bin/usr/local/bin', '/usr/sbin',
        '/sbin/usr/local/sbin']
    for path in default_paths:
        if path not in search_paths:
            search_paths.append(path)
    for path in search_paths:
        if os.path.isdir(path):
            filename = os.path.join(path, binary_name)
            if os.path.exists(filename):
                return filename
    return binary