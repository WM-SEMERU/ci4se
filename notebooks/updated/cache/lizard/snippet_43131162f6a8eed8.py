def _verify_authentication(self, handler, args, kwargs):
    if not self.user_manager.session_logged_in():
        raise APIForbidden()
    return handler(*args, **kwargs)