def create_session(self, callback, monitor_id):
    self.log.info('Creating Session for Monitor %s.' % monitor_id)
    session = SecurePushSession(callback, monitor_id, self, self._ca_certs
        ) if self._secure else PushSession(callback, monitor_id, self)
    session.start()
    self.sessions[session.socket.fileno()] = session
    self._init_threads()
    return session