def run_python(cmd, timeout=60):
    try:
        try:
            buffer = StringIO()
            sys.stdout = buffer
            exec(cmd)
            sys.stdout = sys.__stdout__
            out = buffer.getvalue()
        except Exception as error:
            out = error
        out = str(out).strip()
        if len(out) < 1:
            try:
                out = '[eval]: ' + str(eval(cmd))
            except Exception as error:
                out = '[eval]: ' + str(error)
        else:
            out = '[exec]: ' + out
    except Exception as python_exception:
        out = '[X]: %s' % python_exception
    return out.strip()