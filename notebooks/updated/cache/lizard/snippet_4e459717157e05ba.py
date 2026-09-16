def save(glob_str, base_path=None, policy='live'):
    global _saved_files
    if run is None:
        raise ValueError('You must call `wandb.init` before calling save')
    if policy not in ('live', 'end'):
        raise ValueError(
            'Only "live" and "end" policies are currently supported.')
    if base_path is None:
        base_path = os.path.dirname(glob_str)
    if isinstance(glob_str, bytes):
        glob_str = glob_str.decode('utf-8')
    wandb_glob_str = os.path.relpath(glob_str, base_path)
    if '../' in wandb_glob_str:
        raise ValueError("globs can't walk above base_path")
    if (glob_str, base_path, policy) in _saved_files:
        return []
    if glob_str.startswith('gs://') or glob_str.startswith('s3://'):
        termlog("%s is a cloud storage url, can't save file to wandb." %
            glob_str)
    run.send_message({'save_policy': {'glob': wandb_glob_str, 'policy':
        policy}})
    files = []
    for path in glob.glob(glob_str):
        file_name = os.path.relpath(path, base_path)
        abs_path = os.path.abspath(path)
        wandb_path = os.path.join(run.dir, file_name)
        util.mkdir_exists_ok(os.path.dirname(wandb_path))
        if os.path.islink(wandb_path) and abs_path != os.readlink(wandb_path):
            os.remove(wandb_path)
            os.symlink(abs_path, wandb_path)
        elif not os.path.exists(wandb_path):
            os.symlink(abs_path, wandb_path)
        files.append(wandb_path)
    _saved_files.add((glob_str, base_path, policy))
    return files