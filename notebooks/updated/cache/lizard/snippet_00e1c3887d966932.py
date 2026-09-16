def generate_or_read_from_file(key_file='.secret_key', key_length=64):
    abspath = os.path.abspath(key_file)
    if os.path.exists(key_file):
        key = read_from_file(key_file)
        return key
    lock = lockutils.external_lock(key_file + '.lock', lock_path=os.path.
        dirname(abspath))
    with lock:
        if not os.path.exists(key_file):
            key = generate_key(key_length)
            old_umask = os.umask(127)
            with open(key_file, 'w') as f:
                f.write(key)
            os.umask(old_umask)
        else:
            key = read_from_file(key_file)
        return key