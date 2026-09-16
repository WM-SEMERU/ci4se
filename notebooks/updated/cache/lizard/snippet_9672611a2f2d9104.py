def traceback_string():
    tb_string = None
    exc_type, exc_value, exc_traceback = traceback.sys.exc_info()
    if exc_type is not None:
        display_lines_list = [str(exc_value)] + traceback.format_tb(
            exc_traceback)
        tb_string = '\n'.join(display_lines_list)
    return tb_string