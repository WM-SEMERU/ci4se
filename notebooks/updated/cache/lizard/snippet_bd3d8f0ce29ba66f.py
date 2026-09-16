def get_build_files_family(project_tree, dir_relpath, build_ignore_patterns
    =None):
    build_files = set()
    for build in sorted(project_tree.glob1(dir_relpath, '{prefix}*'.format(
        prefix=BuildFile._BUILD_FILE_PREFIX))):
        if BuildFile._is_buildfile_name(build) and project_tree.isfile(os.
            path.join(dir_relpath, build)):
            build_files.add(os.path.join(dir_relpath, build))
    return BuildFile._build_files_from_paths(project_tree, build_files,
        build_ignore_patterns)