def get_resources_dests(resources_root, rules):

    def get_rel_path(base, path):
        base = base.replace(os.path.sep, '/')
        path = path.replace(os.path.sep, '/')
        assert path.startswith(base)
        return path[len(base):].lstrip('/')
    destinations = {}
    for base, suffix, dest in rules:
        prefix = os.path.join(resources_root, base)
        for abs_base in iglob(prefix):
            abs_glob = os.path.join(abs_base, suffix)
            for abs_path in iglob(abs_glob):
                resource_file = get_rel_path(resources_root, abs_path)
                if dest is None:
                    destinations.pop(resource_file, None)
                else:
                    rel_path = get_rel_path(abs_base, abs_path)
                    rel_dest = dest.replace(os.path.sep, '/').rstrip('/')
                    destinations[resource_file] = rel_dest + '/' + rel_path
    return destinations