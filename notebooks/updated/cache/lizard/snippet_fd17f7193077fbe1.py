def walk_dir(path, args, state):
    if args.debug:
        sys.stderr.write('Walking %s\n' % path)
    for root, _dirs, files in os.walk(path):
        if not safe_process_files(root, files, args, state):
            return False
        if state.should_quit():
            return False
    return True