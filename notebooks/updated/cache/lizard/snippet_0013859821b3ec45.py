def new_session(self, server=None, session_name=None, user_name=None,
    existing_session=None):
    if not server:
        server = os.environ.get('STC_SERVER_ADDRESS')
        if not server:
            raise EnvironmentError('STC_SERVER_ADDRESS not set')
    self._stc = stchttp.StcHttp(server)
    if not session_name:
        session_name = os.environ.get('STC_SESSION_NAME')
        if not session_name or session_name == '__NEW_TEST_SESSION__':
            session_name = None
    if not user_name:
        try:
            user_name = getpass.getuser()
        except:
            pass
    if not existing_session:
        existing_session = os.environ.get('EXISTING_SESSION')
    if existing_session:
        existing_session = existing_session.lower()
        if existing_session == 'kill':
            self._stc.new_session(user_name, session_name, True)
            return self._stc
        if existing_session == 'join':
            try:
                self._stc.new_session(user_name, session_name, False)
            except RuntimeError as e:
                if str(e).find('already exists') >= 0:
                    sid = ' - '.join((session_name, user_name))
                    self._stc.join_session(sid)
                else:
                    raise
            return self._stc
    self._stc.new_session(user_name, session_name, False)
    return self._stc