def showsyntaxerror(self, filename=None):
    type, value, tb = sys.exc_info()
    sys.last_type = type
    sys.last_value = value
    sys.last_traceback = tb
    if filename and type is SyntaxError:
        try:
            msg, (dummy_filename, lineno, offset, line) = value.args
        except ValueError:
            pass
        else:
            value = SyntaxError(msg, (filename, lineno, offset, line))
            sys.last_value = value
    list = traceback.format_exception_only(type, value)
    sys.stderr.write(''.join(list))