def exceptions(error_is_fatal=True, error_messages=None):

    def exception_decorator(func):
        nonlocal error_messages

        @functools.wraps(func)
        def exc_wrapper(*args, **kwargs):
            nonlocal error_messages
            try:
                result = func(*args, **kwargs)
            except sa.exc.SQLAlchemyError as err:
                result = None
                details = None
                err_type = err.__class__
                if error_messages and err_type in error_messages:
                    details = error_messages[err_type]
                if details:
                    LOG.error(details)
                LOG.error('For developers: (%s) %s', err.__class__, str(err))
                if error_is_fatal:
                    sys.exit('Abort, SQL operation failed.')
                if not ui.ask(
                    'I can continue at your own risk, do you want that?'):
                    raise err
            return result
        return exc_wrapper
    return exception_decorator