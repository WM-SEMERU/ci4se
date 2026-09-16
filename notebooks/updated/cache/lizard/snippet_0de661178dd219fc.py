def cp(src_path, dst_path, follow_links=False, recursive=True):
    successful = False
    try:
        if follow_links and os.path.islink(src_path):
            src_path = os.path.realpath(src_path)
        if follow_links and os.path.islink(dst_path):
            dst_path = os.path.realpath(dst_path)
        if os.path.isdir(src_path):
            if not recursive:
                return successful
            shutil.copytree(src_path, dst_path, symlinks=follow_links)
            successful = True
        elif os.path.exists(src_path):
            if os.path.isdir(dst_path):
                dst_path = os.path.join(dst_path, os.path.basename(src_path))
            shutil.copy2(src_path, dst_path)
            successful = True
        else:
            log.error('cp: source not found: %s' % src_path)
    except (OSError, TypeError) as error:
        log.error('cp: execute failed: %s => %s (%s)' % (src_path, dst_path,
            error))
    return successful