def record(self):
    if self.recordmetadata:
        return Record(self.recordmetadata.json, model=self.recordmetadata)
    else:
        return None