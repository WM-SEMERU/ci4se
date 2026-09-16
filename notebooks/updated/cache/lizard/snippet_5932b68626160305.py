def has_pinned_content(self):
    if 'query' in self.query:
        q = self.query['query']
    else:
        q = self.query
    if 'pinned_ids' in q:
        return bool(len(q.get('pinned_ids', [])))
    return False