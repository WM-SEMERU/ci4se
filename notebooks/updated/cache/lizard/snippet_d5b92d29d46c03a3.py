def optional_manga_logged_in(func):

    @functools.wraps(func)
    @require_session_started
    def inner_func(self, *pargs, **kwargs):
        if not self._manga_api.logged_in and self.has_credentials:
            logger.info(
                'Logging into android manga API for optional meta method')
            self._manga_api.cr_login(account=self._state['username'],
                password=self._state['password'])
        return func(self, *pargs, **kwargs)
    return inner_func