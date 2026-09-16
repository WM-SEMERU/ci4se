def select(self, select, table_name, where=None, extra=None):
    self.verify_table_existence(table_name)
    return self.execute_query(six.text_type(Select(select, table_name,
        where, extra)), logging.getLogger().findCaller())