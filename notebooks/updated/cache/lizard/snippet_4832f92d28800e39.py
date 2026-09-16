def delete_entries(self, entries):
    self.lines = trim([line for line in self.lines if not isinstance(line,
        Entry) or line not in entries])