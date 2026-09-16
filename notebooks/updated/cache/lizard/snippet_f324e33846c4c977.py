def _compute_approver_group_ids(self):
    for page in self:
        res = page.approver_gid
        if page.parent_id:
            res = res | page.parent_id.approver_group_ids
        page.approver_group_ids = res