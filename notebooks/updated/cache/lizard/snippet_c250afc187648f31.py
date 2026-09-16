def new_revision(self, *fields):
    if not self._id:
        assert g.get('draft'
            ), 'Only draft documents can be assigned new revisions'
    else:
        with self.draft_context():
            assert self.count(Q._id == self._id
                ) == 1, 'Only draft documents can be assigned new revisions'
    if len(fields) > 0:
        fields.append('revision')
    self.revision = datetime.now()
    self.upsert(*fields)