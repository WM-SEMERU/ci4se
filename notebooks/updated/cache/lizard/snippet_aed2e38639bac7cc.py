def log_fault_info_str(exc_info, message='', level=logging.CRITICAL,
    traceback=False):
    tb = sys.exc_info()[2]
    stack = _get_stack(tb)
    rc = StringIO()
    rc.write('%s: FAULT: %s%s(%s): %s\n' % (logging.getLevelName(level), 
        '%s -- ' % message if message else '', tb.tb_frame.f_code.
        co_filename, tb.tb_lineno, repr(exc_info[1])))
    if traceback:
        for line in _generate_stackdump(stack):
            rc.write('%s\n' % line)
    return rc.getvalue()