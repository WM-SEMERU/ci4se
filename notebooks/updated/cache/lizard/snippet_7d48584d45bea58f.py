def insert_child(self, child_pid, index=-1):
    if child_pid.status != PIDStatus.REGISTERED:
        raise PIDRelationConsistencyError(
            "Version PIDs should have status 'REGISTERED'. Use insert_draft_child to insert 'RESERVED' draft PID."
            )
    with db.session.begin_nested():
        draft = self.draft_child
        if draft and index == -1:
            index = self.index(draft)
        super(PIDNodeVersioning, self).insert_child(child_pid, index=index)
        self.update_redirect()