def delete_policy(self, scaling_group, policy):
    return self._manager.delete_policy(scaling_group=scaling_group, policy=
        policy)