def _format_exception_message(e):
    if isinstance(e, dxpy.AppError):
        return _safe_unicode(e)
    if USING_PYTHON2:
        return unicode(e.__class__.__name__, 'utf-8') + ': ' + _safe_unicode(e)
    else:
        return e.__class__.__name__ + ': ' + _safe_unicode(e)