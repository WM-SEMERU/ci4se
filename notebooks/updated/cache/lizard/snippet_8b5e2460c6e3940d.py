def cleanup_files(patterns, dry_run=False, workdir='.'):
    current_dir = Path(workdir)
    python_basedir = Path(Path(sys.executable).dirname()).joinpath('..'
        ).abspath()
    error_message = None
    error_count = 0
    for file_pattern in patterns:
        for file_ in path_glob(file_pattern, current_dir):
            if file_.abspath().startswith(python_basedir):
                continue
            if dry_run:
                print('REMOVE: %s (dry-run)' % file_)
            else:
                print('REMOVE: %s' % file_)
                try:
                    file_.remove_p()
                except os.error as e:
                    message = '%s: %s' % (e.__class__.__name__, e)
                    print(message + ' basedir: ' + python_basedir)
                    error_count += 1
                    if not error_message:
                        error_message = message
    if False and error_message:


        class CleanupError(RuntimeError):
            pass
        raise CleanupError(error_message)