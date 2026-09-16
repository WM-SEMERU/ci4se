def _scons_internal_warning(e):
    filename, lineno, routine, dummy = find_deepest_user_frame(traceback.
        extract_stack())
    sys.stderr.write('\nscons: warning: %s\n' % e.args[0])
    sys.stderr.write('File "%s", line %d, in %s\n' % (filename, lineno,
        routine))