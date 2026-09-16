def disconnect(self, abandon_session=False):
    self.connected = False
    if self.session and self.session.is_expired or abandon_session:
        try:
            self.logout()
        except:
            log.warning(
                'Logout call to responsys failed, session may have not been terminated'
                , exc_info=True)
        del self.session
    return True