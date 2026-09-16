def clean(ctx, dry_run=False):
    directories = ctx.clean.directories
    files = ctx.clean.files
    extra_directories = ctx.clean.extra_directories or []
    extra_files = ctx.clean.extra_files or []
    if extra_directories:
        directories.extend(extra_directories)
    if extra_files:
        files.extend(extra_files)
    execute_cleanup_tasks(ctx, cleanup_tasks, dry_run=dry_run)
    cleanup_dirs(directories, dry_run=dry_run)
    cleanup_files(files, dry_run=dry_run)