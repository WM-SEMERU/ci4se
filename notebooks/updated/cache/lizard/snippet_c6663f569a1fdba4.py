def count_documents(self, filter={}, *args, **kwargs):
    result = self.collection.count_documents(filter, *args, **kwargs)
    return result