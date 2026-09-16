def discover(glob_pattern):
    in_paths = glob.glob(glob_pattern)
    names = {extract_env_name(path): path for path in in_paths}
    return order_by_refs([{'name': name, 'refs': Environment.
        parse_references(in_path)} for name, in_path in names.items()])