def python_console(namespace=None):
    if namespace is None:
        import inspect
        frame = inspect.currentframe()
        caller = frame.f_back
        if not caller:
            logging.error("can't find caller who start this console.")
            caller = frame
        namespace = dict(caller.f_globals)
        namespace.update(caller.f_locals)
    return get_python_console(namespace=namespace).interact()