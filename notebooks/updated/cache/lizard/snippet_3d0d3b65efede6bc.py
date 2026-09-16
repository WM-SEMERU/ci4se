def copytree_atomic(source_path, dest_path, make_parents=False,
    backup_suffix=None, symlinks=False):
    if os.path.isdir(source_path):
        with atomic_output_file(dest_path, make_parents=make_parents,
            backup_suffix=backup_suffix) as tmp_path:
            shutil.copytree(source_path, tmp_path, symlinks=symlinks)
    else:
        copyfile_atomic(source_path, dest_path, make_parents=make_parents,
            backup_suffix=backup_suffix)