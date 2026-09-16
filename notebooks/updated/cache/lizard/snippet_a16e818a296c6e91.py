def can_publish(self):
    with self.published_context():
        published = self.one(Q._uid == self._uid, projection={'revision': True}
            )
    if not published:
        return True
    with self.draft_context():
        draft = self.one(Q._uid == self._uid, projection={'revision': True})
    return draft.revision > published.revision