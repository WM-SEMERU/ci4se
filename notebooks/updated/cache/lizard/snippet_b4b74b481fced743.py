def _read_import_root_map_file(path):
    if os.path.exists(path):
        with open(path, 'r') as fp:
            return dict({import_path: root for import_path, root in (x.
                strip().split('\t') for x in fp.readlines())})
    else:
        return {}