def run_transaction(transactor, callback):
    if isinstance(transactor, sqlalchemy.engine.Connection):
        return _txn_retry_loop(transactor, callback)
    elif isinstance(transactor, sqlalchemy.engine.Engine):
        with transactor.connect() as connection:
            return _txn_retry_loop(connection, callback)
    elif isinstance(transactor, sqlalchemy.orm.sessionmaker):
        session = transactor(autocommit=True)
        return _txn_retry_loop(session, callback)
    else:
        raise TypeError("don't know how to run a transaction on %s", type(
            transactor))