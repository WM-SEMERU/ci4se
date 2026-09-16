def exception(maxTBlevel=None):
    try:
        from marrow.util.bunch import Bunch
        cls, exc, trbk = sys.exc_info()
        excName = cls.__name__
        excArgs = getattr(exc, 'args', None)
        excTb = ''.join(traceback.format_exception(cls, exc, trbk, maxTBlevel))
        return Bunch(name=excName, cls=cls, exception=exc, trace=trbk,
            formatted=excTb, args=excArgs)
    finally:
        del cls, exc, trbk