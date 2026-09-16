def _item_to_database(self, iterator, database_pb):
    return Database.from_pb(database_pb, self, pool=BurstyPool())