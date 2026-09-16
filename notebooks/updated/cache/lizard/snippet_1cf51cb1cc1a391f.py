def fetch(self):
    try:
        with self.gen_lock(lock_type='update'):
            log.debug("Fetching %s remote '%s'", self.role, self.id)
            return self._fetch()
    except GitLockError as exc:
        if exc.errno == errno.EEXIST:
            log.warning(
                "Update lock file is present for %s remote '%s', skipping. If this warning persists, it is possible that the update process was interrupted, but the lock could also have been manually set. Removing %s or running 'salt-run cache.clear_git_lock %s type=update' will allow updates to continue for this remote."
                , self.role, self.id, self._get_lock_file(lock_type=
                'update'), self.role)
        return False