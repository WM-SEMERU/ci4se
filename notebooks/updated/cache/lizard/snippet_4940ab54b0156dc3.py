def count(self, signature=None):
    query = self._session.query(CrashDTO.id)
    if signature:
        sig_pickled = pickle.dumps(signature, protocol=0)
        query = query.filter_by(signature=sig_pickled)
    return query.count()