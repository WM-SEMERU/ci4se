def serializeCorpus(self):
    corpus_details = [{'model': 'django-tethne.corpus', 'pk': self.
        corpus_id, 'fields': {'source': self.source, 'date_created':
        strftime('%Y-%m-%d %H:%M:%S', gmtime()), 'length': len(self.corpus)}}]
    return corpus_details