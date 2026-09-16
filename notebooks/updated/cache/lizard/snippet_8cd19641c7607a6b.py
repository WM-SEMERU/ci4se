def get_unspent_outputs(self):
    cursor = backend.query.get_unspent_outputs(self.connection)
    return (record for record in cursor)