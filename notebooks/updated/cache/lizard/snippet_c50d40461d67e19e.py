def decompress(self, value):
    if hasattr(value, 'select_related'):
        keywords = [a.keyword for a in value.select_related('keyword')]
        if keywords:
            keywords = [(str(k.id), k.title) for k in keywords]
            self._ids, words = list(zip(*keywords))
            return ','.join(self._ids), ', '.join(words)
    return '', ''