def update_or_append_line(filename, prefix, new_line, keep_backup=True,
    append=True):
    result = None
    if env.host_string == 'localhost':
        result = update_or_append_local(filename, prefix, new_line,
            keep_backup, append)
    else:
        tmp_dir = tempfile.mkdtemp(suffix='', prefix='fabsetup_')
        local_path = os.path.join(tmp_dir, os.path.basename(filename))
        fabric.operations.get(remote_path=filename, local_path=local_path,
            use_sudo=True, temp_dir='/tmp')
        result = update_or_append_local(local_path, prefix, new_line,
            keep_backup, append)
        put(local_path, remote_path=filename, use_sudo=True, temp_dir='/tmp')
        with quiet():
            fabric.api.local(flo('rm -rf {tmp_dir}'))
    return result