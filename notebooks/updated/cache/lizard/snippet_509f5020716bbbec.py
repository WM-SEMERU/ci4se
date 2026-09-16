def check_basename_conflicts(self, targets):
    basename_seen = {}
    for target in targets:
        if target.basename in basename_seen:
            raise self.BasenameConflictError(
                """Basename must be unique, found two targets use the same basename: {}'
	{} and 
	{}"""
                .format(target.basename, basename_seen[target.basename].
                address.spec, target.address.spec))
        basename_seen[target.basename] = target