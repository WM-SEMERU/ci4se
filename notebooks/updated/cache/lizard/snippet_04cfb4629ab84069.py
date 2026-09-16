def session_info(self, session):
    _, sp_hkey = self._keygen(session)
    picked_event = self.r.hgetall(sp_hkey)
    event = {s(k): pickle.loads(v) for k, v in picked_event.items()}
    return event