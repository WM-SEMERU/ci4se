def run(self):
    if not (self.table and self.columns):
        raise Exception('table and columns need to be specified')
    connection = self.output().connect()
    for attempt in range(2):
        try:
            cursor = connection.cursor()
            print('caling init copy...')
            self.init_copy(connection)
            self.copy(cursor)
            self.post_copy(connection)
            if self.enable_metadata_columns:
                self.post_copy_metacolumns(cursor)
        except Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE and attempt == 0:
                connection.reconnect()
                self.create_table(connection)
            else:
                raise
        else:
            break
    self.output().touch(connection)
    connection.commit()
    connection.close()