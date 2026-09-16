def delete(self, uri, query=None, **kwargs):
    return self.fetch('delete', uri, query, **kwargs)