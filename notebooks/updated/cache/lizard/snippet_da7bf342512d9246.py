def create_build_process(process_type, working_dir, build_system, package=
    None, vcs=None, ensure_latest=True, skip_repo_errors=False,
    ignore_existing_tag=False, verbose=False, quiet=False):
    from rez.plugin_managers import plugin_manager
    process_types = get_build_process_types()
    if process_type not in process_types:
        raise BuildProcessError('Unknown build process: %r' % process_type)
    cls = plugin_manager.get_plugin_class('build_process', process_type)
    return cls(working_dir, build_system, package=package, vcs=vcs,
        ensure_latest=ensure_latest, skip_repo_errors=skip_repo_errors,
        ignore_existing_tag=ignore_existing_tag, verbose=verbose, quiet=quiet)