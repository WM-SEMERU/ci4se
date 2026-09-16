def create_index(self):
    es = self._init_connection()
    if not es.indices.exists(index=self.index):
        es.indices.create(index=self.index, body=self.settings)