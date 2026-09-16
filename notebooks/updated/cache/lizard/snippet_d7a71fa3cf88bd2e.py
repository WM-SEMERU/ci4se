def get_publisher_doc(self):
    with self.draft_context():
        draft = self.one(Q._uid == self._uid)
        publisher_doc = draft._document
        self._remove_keys(publisher_doc, self._unpublished_fields)
    return publisher_doc