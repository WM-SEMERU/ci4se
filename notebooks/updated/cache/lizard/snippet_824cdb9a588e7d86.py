def revert(self, revision_id):
    if self.model is None:
        raise MissingModelError()
    revision = self.revisions[revision_id]
    with db.session.begin_nested():
        before_record_revert.send(current_app._get_current_object(), record
            =self)
        self.model.json = dict(revision)
        db.session.merge(self.model)
    after_record_revert.send(current_app._get_current_object(), record=self)
    return self.__class__(self.model.json, model=self.model)