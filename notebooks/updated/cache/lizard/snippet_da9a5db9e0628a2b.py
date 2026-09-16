def _init_flow_exceptions():
    global _flow_exceptions
    _flow_exceptions = ()
    add_flow_exception(datastore_errors.Rollback)
    try:
        from webob import exc
    except ImportError:
        pass
    else:
        add_flow_exception(exc.HTTPException)