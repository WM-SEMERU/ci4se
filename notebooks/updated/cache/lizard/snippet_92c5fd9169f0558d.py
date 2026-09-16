def drop():
    _State.connection()
    _State.table.drop(checkfirst=True)
    _State.metadata.remove(_State.table)
    _State.table = None
    _State.new_transaction()