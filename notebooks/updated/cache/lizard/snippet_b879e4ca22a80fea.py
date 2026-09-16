def insert_many(self, rows, chunk_size=1000, ensure=None, types=None):
    chunk = []
    for row in rows:
        row = self._sync_columns(row, ensure, types=types)
        chunk.append(row)
        if len(chunk) == chunk_size:
            chunk = pad_chunk_columns(chunk)
            self.table.insert().execute(chunk)
            chunk = []
    if len(chunk):
        chunk = pad_chunk_columns(chunk)
        self.table.insert().execute(chunk)