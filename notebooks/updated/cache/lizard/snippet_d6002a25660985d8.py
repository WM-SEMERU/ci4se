def _safe_import(module_name):


    class _Null(object):

        def write(self, *_):
            pass
    sout, serr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = _Null(), _Null()
    try:
        m = import_module(module_name)
    except:
        m = None
    sys.stdout, sys.stderr = sout, serr
    return m