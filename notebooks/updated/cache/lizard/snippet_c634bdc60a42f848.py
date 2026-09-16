def find_static_library(library_name, library_path):
    variants = ['lib{0}.a', '{0}.a', '{0}.lib', 'lib{0}.lib']
    if is_unix_like():
        extra_libdirs = ['/usr/local/lib64', '/usr/local/lib', '/usr/lib64',
            '/usr/lib', '/lib64', '/lib']
    else:
        extra_libdirs = []
    for path in extra_libdirs:
        if path not in library_path and os.path.isdir(path):
            library_path.append(path)
    for path in library_path:
        for variant in variants:
            full_path = os.path.join(path, variant.format(library_name))
            if os.path.isfile(full_path):
                return full_path