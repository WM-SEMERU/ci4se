def delete(self, table, where=None):
    if where:
        where_key, where_val = where
        query = "DELETE FROM {0} WHERE {1}='{2}'".format(wrap(table),
            where_key, where_val)
    else:
        query = 'DELETE FROM {0}'.format(wrap(table))
    self.execute(query)
    return True