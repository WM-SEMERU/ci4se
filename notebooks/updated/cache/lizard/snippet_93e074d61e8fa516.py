def upload(remote_location, remotes=None, ignores=None, static_root=
    '/static/', prefix='', dry_run=False):
    if remotes is None:
        remotes, ignores = _resources_files(abs_paths=remote_location.
            startswith('s3://'))
    if remote_location.startswith('s3://'):
        from deployutils.s3 import S3Backend
        backend = S3Backend(remote_location, static_root=static_root,
            dry_run=dry_run)
        backend.upload(list_local(remotes, prefix), prefix)
    else:
        excludes = []
        if ignores:
            for ignore in ignores:
                excludes += ['--exclude', ignore]
        shell_command(['/usr/bin/rsync'] + excludes + ['-pOthrRvz',
            '--rsync-path', '/usr/bin/rsync'] + remotes + [remote_location],
            dry_run=dry_run)