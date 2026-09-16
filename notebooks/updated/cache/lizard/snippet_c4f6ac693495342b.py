def uninstall(**kwargs):
    force = kwargs.get('force')
    restore_legacy = kwargs.get('restore_legacy')
    colorama.init(strip=kwargs.get('no_color'))
    git_dir = current_git_dir()
    if git_dir is None:
        output(NOT_GIT_REPO_MSG)
        exit(1)
    hook_path = os.path.join(git_dir, 'hooks', 'pre-commit')
    if not os.path.isfile(hook_path):
        output(NO_HOOK_INSTALLED_MSG)
        exit(0)
    hook_hash = identify_hook(hook_path)
    if hook_hash:
        if not force:
            if not click.confirm(CONFIRM_UNINSTALL_HOOK_MSG, default=False):
                output(UNINSTALL_ABORTED_MSG)
                exit(1)
    else:
        output(CURRENT_HOOK_NOT_THERAPIST_MSG)
        exit(1)
    legacy_hook_path = os.path.join(git_dir, 'hooks', 'pre-commit.legacy')
    if os.path.isfile(legacy_hook_path):
        if not force and not restore_legacy:
            output(LEGACY_HOOK_EXISTS_MSG)
            restore_legacy = click.confirm(CONFIRM_RESTORE_LEGACY_HOOK_MSG,
                default=True)
        if restore_legacy:
            output(COPYING_LEGACY_HOOK_MSG, end='')
            shutil.copy2(legacy_hook_path, hook_path)
            os.remove(legacy_hook_path)
            output(DONE_COPYING_LEGACY_HOOK_MSG)
            exit(0)
        elif force or click.confirm('Would you like to remove the legacy hook?'
            , default=False):
            output(REMOVING_LEGACY_HOOK_MSG, end='')
            os.remove(legacy_hook_path)
            output(DONE_REMOVING_LEGACY_HOOK_MSG)
    output(UNINSTALLING_HOOK_MSG, end='')
    os.remove(hook_path)
    output(DONE_UNINSTALLING_HOOK_MSG)