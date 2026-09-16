def _cycle_proceedings(self):
    next_approvals = self._get_next_approvals().exclude(status=PENDING
        ).exclude(cloned=True)
    for ta in next_approvals:
        clone_transition_approval, c = (TransitionApproval.objects.
            get_or_create(source_state=ta.source_state, destination_state=
            ta.destination_state, content_type=ta.content_type, object_id=
            ta.object_id, field_name=ta.field_name, skip=ta.skip, priority=
            ta.priority, enabled=ta.enabled, status=PENDING, meta=ta.meta))
        if c:
            clone_transition_approval.permissions.add(*ta.permissions.all())
            clone_transition_approval.groups.add(*ta.groups.all())
        next_approvals.update(cloned=True)
    return True if next_approvals.count() else False