def create(self, data):
    q = self.history.insert_one(data).inserted_id
    logging.debug(self.history.find_one({'_id': q}))