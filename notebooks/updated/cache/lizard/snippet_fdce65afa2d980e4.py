def clean_python(ctx, dry_run=False):
    cleanup_dirs(['build', 'dist', '*.egg-info', '**/__pycache__'], dry_run
        =dry_run)
    if not dry_run:
        ctx.run('py.cleanup')
    cleanup_files(['**/*.pyc', '**/*.pyo', '**/*$py.class'], dry_run=dry_run)