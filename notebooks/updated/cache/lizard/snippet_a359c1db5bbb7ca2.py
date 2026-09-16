def create_marker_index(self):
    if not self.es.indices.exists(index=self.marker_index):
        self.es.indices.create(index=self.marker_index)