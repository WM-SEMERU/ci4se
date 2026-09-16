def commit(self, session):
    sp_key, sp_hkey = self._keygen(session)
    with self.r.pipeline(transaction=False) as p:
        p.srem(sp_key, session.meepo_unique_id)
        p.expire(sp_hkey, 60 * 60)
        p.execute()