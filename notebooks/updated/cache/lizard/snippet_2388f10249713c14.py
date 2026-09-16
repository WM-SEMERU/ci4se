def _ivy_resolve(self, targets, executor=None, silent=False, workunit_name=
    None, confs=None, extra_args=None, invalidate_dependents=False,
    pinned_artifacts=None):
    if not targets:
        return NO_RESOLVE_RUN_RESULT
    confs = confs or ('default',)
    fingerprint_strategy = IvyResolveFingerprintStrategy(confs)
    with self.invalidated(targets, invalidate_dependents=
        invalidate_dependents, silent=silent, fingerprint_strategy=
        fingerprint_strategy) as invalidation_check:
        if not invalidation_check.all_vts:
            return NO_RESOLVE_RUN_RESULT
        resolve_vts = VersionedTargetSet.from_versioned_targets(
            invalidation_check.all_vts)
        resolve_hash_name = resolve_vts.cache_key.hash
        ivy_workdir = os.path.join(self.versioned_workdir, 'ivy')
        targets = resolve_vts.targets
        fetch = IvyFetchStep(confs, resolve_hash_name, pinned_artifacts,
            self.get_options().soft_excludes, self.ivy_resolution_cache_dir,
            self.ivy_repository_cache_dir, ivy_workdir)
        resolve = IvyResolveStep(confs, resolve_hash_name, pinned_artifacts,
            self.get_options().soft_excludes, self.ivy_resolution_cache_dir,
            self.ivy_repository_cache_dir, ivy_workdir)
        return self._perform_resolution(fetch, resolve, executor,
            extra_args, invalidation_check, resolve_vts, targets, workunit_name
            )