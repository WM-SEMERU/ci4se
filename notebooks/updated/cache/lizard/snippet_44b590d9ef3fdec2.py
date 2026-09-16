def apply_postcompilers(root, src_list, dst, processors):
    dst_file = os.path.join(root, dst)
    matches = [(pattern, cmds) for pattern, cmds in processors.iteritems() if
        fnmatch(dst, pattern)]
    if not matches:
        ensure_dirs(dst_file)
        logger.info('Combining [%s] into [%s]', ' '.join(src_list), dst_file)
        with open(dst_file, 'w') as dst_fp:
            for src in src_list:
                with open(os.path.join(root, src)) as src_fp:
                    for chunk in src_fp:
                        dst_fp.write(chunk)
        return True
    params = get_format_params(dst)
    src_names = src_list
    for pattern, cmd_list in matches:
        for cmd in cmd_list:
            run_command(cmd, root=root, dst=dst, input=' '.join(src_names),
                params=params)
            src_names = [dst]
    return True