def save_session(self, sid, session, namespace=None):
    namespace = namespace or '/'
    eio_session = self.eio.get_session(sid)
    eio_session[namespace] = session