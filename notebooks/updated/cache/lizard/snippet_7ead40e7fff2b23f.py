def append(self, x):
    super(EntriesList, self).append(x)
    if self.entries_collection is not None:
        self.entries_collection.add_entry(self.date, x)