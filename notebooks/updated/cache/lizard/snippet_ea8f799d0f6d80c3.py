def _sync_directories(from_directory, to_directory):
    if not os.path.exists(to_directory):
        os.mkdir(to_directory)
    for root, dirs, files in os.walk(from_directory):
        to_root = root.replace(from_directory, to_directory)
        for directory in dirs:
            to_child_dir = os.path.join(to_root, directory)
            if not os.path.exists(to_child_dir):
                os.mkdir(to_child_dir)
        for fname in files:
            from_file = os.path.join(root, fname)
            to_file = os.path.join(to_root, fname)
            with open(from_file, 'rb') as a, open(to_file, 'wb') as b:
                b.write(a.read())