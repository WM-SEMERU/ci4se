def put(self, session):
    if self._sessions.full():
        raise queue.Full
    txn = session._transaction
    if txn is None or txn.committed() or txn._rolled_back:
        session.transaction()
        self._pending_sessions.put(session)
    else:
        super(TransactionPingingPool, self).put(session)