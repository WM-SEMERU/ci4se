def get_session_value(self, name, default=None):
    session_name = 'list_{}_{}_{}'.format(self.kwargs.get('app'), self.
        kwargs.get('model'), name)
    return self.request.session.get(session_name, default)