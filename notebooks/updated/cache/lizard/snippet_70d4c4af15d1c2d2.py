def update_snapshot_policy(self, name, policy):
    return self._put('snapshots/policies/%s' % name, ApiSnapshotPolicy,
        data=policy, api_version=6)