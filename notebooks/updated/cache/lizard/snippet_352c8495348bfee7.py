def _fqdn(o, oset=True, recheck=False, pmodule=None):
    if id(o) in _set_failures or o is None:
        return None
    if recheck or not _safe_hasattr(o, '__fqdn__'):
        import inspect
        if not hasattr(o, '__name__'):
            msg.warn('Skipped object {}: no __name__ attribute.'.format(o), 3)
            return
        result = None
        if hasattr(o, '__acornext__') and o.__acornext__ is not None:
            otarget = o.__acornext__
        else:
            otarget = o
        omod = _safe_getmodule(otarget) or pmodule
        if omod is None and hasattr(otarget, '__objclass__'
            ) and otarget.__objclass__ is not None:
            omod = _safe_getmodule(otarget.__objclass__)
            parts = ('<unknown>' if omod is None else omod.__name__,
                otarget.__objclass__.__name__, otarget.__name__)
            result = '{}.{}.{}'.format(*parts)
        elif omod is None and hasattr(otarget, '__class__'
            ) and otarget.__class__ is not None:
            omod = _safe_getmodule(otarget.__class__)
            parts = ('<unknown>' if omod is None else omod.__name__,
                otarget.__class__.__name__, otarget.__name__)
            result = '{}.{}.{}'.format(*parts)
        elif omod is not otarget:
            parts = _fqdn(omod, False), otarget.__name__
            result = '{}.{}'.format(*parts)
        else:
            result = otarget.__name__
        if oset:
            _safe_setattr(o, '__fqdn__', result)
        return result
    if _safe_hasattr(o, '__fqdn__'):
        return o.__fqdn__