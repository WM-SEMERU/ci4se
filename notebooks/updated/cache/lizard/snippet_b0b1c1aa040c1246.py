def select_db(self, db):
    yield self._execute_command(COMMAND.COM_INIT_DB, db)
    yield self._read_ok_packet()