def search(self, word, limit=30):
    search = Search(PrefixQuery('word', word), sort={'count': 'desc'})
    for doc in self.connection.search(search, indexes=[self.index], count=limit
        ):
        yield doc['word'], doc['count']