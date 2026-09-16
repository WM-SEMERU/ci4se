def script(container, script_path, fail_nonzero=False, upload_dir=False, **
    kwargs):
    full_script_path = os.path.abspath(script_path)
    prefix, name = os.path.split(full_script_path)
    with temp_dir() as remote_tmp:
        if upload_dir:
            prefix_path, prefix_name = os.path.split(prefix)
            remote_script = posixpath.join(remote_tmp, prefix_name, name)
            put(prefix, remote_tmp, mirror_local_mode=True)
        else:
            remote_script = posixpath.join(remote_tmp, name)
            put(script_path, remote_script, mirror_local_mode=True)
        results = [output.result for output in container_fabric().
            run_script(container, script_path=remote_script, **kwargs) if o
            .action_type == ContainerUtilAction.SCRIPT]
    for res in results:
        puts('Exit code: {0}'.format(res['exit_code']))
        if res['exit_code'] == 0 or not fail_nonzero:
            puts(res['log'])
        else:
            error(res['log'])