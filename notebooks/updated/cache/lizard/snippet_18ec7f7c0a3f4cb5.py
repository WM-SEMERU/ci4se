def _GetApprovals(self, approval_type, offset, count, filter_func=None,
    token=None):
    approvals_base_urn = aff4.ROOT_URN.Add('users').Add(token.username).Add(
        'approvals').Add(approval_type)
    all_children = aff4.FACTORY.RecursiveMultiListChildren([approvals_base_urn]
        )
    approvals_urns = []
    for subject, children in all_children:
        if children:
            continue
        approvals_urns.append(subject)
    approvals_urns.sort(key=lambda x: x.age, reverse=True)
    approvals = list(aff4.FACTORY.MultiOpen(approvals_urns, mode='r',
        aff4_type=aff4_security.Approval, age=aff4.ALL_TIMES, token=token))
    approvals_by_urn = {}
    for approval in approvals:
        approvals_by_urn[approval.symlink_urn or approval.urn] = approval
    cur_offset = 0
    sorted_approvals = []
    for approval_urn in approvals_urns:
        try:
            approval = approvals_by_urn[approval_urn]
        except KeyError:
            continue
        if filter_func is not None and not filter_func(approval):
            continue
        cur_offset += 1
        if cur_offset <= offset:
            continue
        if count and len(sorted_approvals) >= count:
            break
        sorted_approvals.append(approval)
    subjects_urns = [a.Get(a.Schema.SUBJECT) for a in approvals]
    subjects_by_urn = {}
    for subject in aff4.FACTORY.MultiOpen(subjects_urns, mode='r', token=token
        ):
        subjects_by_urn[subject.urn] = subject
    return sorted_approvals, subjects_by_urn