def flush(self):
    files = self.dumps()
    if files or '_files' in self.record:
        self.record['_files'] = files