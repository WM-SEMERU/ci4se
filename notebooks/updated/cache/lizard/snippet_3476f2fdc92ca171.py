def index_column(self, index_name, table, column):
    cursor = self.get_cursor()
    try:
        cursor.execute('CREATE INDEX {0} on {1}({2})'.format(index_name,
            table, column))
    except sqlite3.OperationalError as error:
        print(error)
        print('Skipping index creation and assuming it exists already')
    else:
        self.conn.commit()