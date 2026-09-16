def local_manager_target_uids(self):
    groups = self.root['groups'].backend
    managed_uids = set()
    for gid in self.local_manager_target_gids:
        group = groups.get(gid)
        if group:
            managed_uids.update(group.member_ids)
    return list(managed_uids)