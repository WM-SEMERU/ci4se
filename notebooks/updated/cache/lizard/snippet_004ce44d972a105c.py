def error(msg, log_file=None):
    UtilClass.print_msg(msg + os.linesep)
    if log_file is not None:
        UtilClass.writelog(log_file, msg, 'append')
    raise RuntimeError(msg)