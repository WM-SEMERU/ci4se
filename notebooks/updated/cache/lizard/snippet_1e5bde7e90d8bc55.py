def enquire_session(self, session=None):
    if session is None:
        session = tf.get_default_session()
        if session is None:
            session = session_manager.get_default_session()
    self.is_built_coherence(session.graph)
    return session