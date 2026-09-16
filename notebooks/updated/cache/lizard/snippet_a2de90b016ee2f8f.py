def _stage_local_files(local_dir, local_files={}):
    staging_dir = os.path.join(tempfile.mkdtemp(), os.path.basename(local_dir))
    os.mkdir(staging_dir)
    for root, dirs, files in os.walk(local_dir):
        relative_tree = root.replace(local_dir, '')
        if relative_tree:
            relative_tree = relative_tree[1:]
        if local_files:
            files = local_files.get(relative_tree, [])
        for file in files:
            if relative_tree:
                filepath = os.path.join(relative_tree, file)
                if not os.path.exists(os.path.join(staging_dir, relative_tree)
                    ):
                    os.mkdir(os.path.join(staging_dir, relative_tree))
            else:
                filepath = file
            shutil.copy2(os.path.join(root, file), os.path.join(staging_dir,
                filepath))
    return staging_dir