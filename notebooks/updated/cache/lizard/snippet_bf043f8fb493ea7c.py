def get_document_eids(self, *args, **kwds):
    search = ScopusSearch('au-id({})'.format(self.author_id), *args, **kwds)
    return search.get_eids()