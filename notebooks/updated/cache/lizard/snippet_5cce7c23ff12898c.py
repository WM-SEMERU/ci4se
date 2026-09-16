def _register_if_needed(cls, run_object):
    if isinstance(run_object, six.string_types):
        return run_object
    elif isinstance(run_object, types.FunctionType):
        if run_object.__name__ == '<lambda>':
            logger.warning(
                'Not auto-registering lambdas - resolving as variant.')
            return run_object
        else:
            name = run_object.__name__
            register_trainable(name, run_object)
            return name
    elif isinstance(run_object, type):
        name = run_object.__name__
        register_trainable(name, run_object)
        return name
    else:
        raise TuneError("Improper 'run' - not string nor trainable.")