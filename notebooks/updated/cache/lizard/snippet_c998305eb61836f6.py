def scoped_session_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        from wallace.db import session as wallace_session
        with sessions_scope(wallace_session) as session:
            from psiturk.db import db_session as psi_session
            with sessions_scope(psi_session) as session_psiturk:
                logger.debug('Running worker %s in scoped DB sessions',
                    func.__name__)
                return func(*args, **kwargs)
    return wrapper