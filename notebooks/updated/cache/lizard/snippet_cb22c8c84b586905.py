def merge(self, revision=None):
    self.create()
    self.ensure_working_tree()
    revision = revision or self.default_revision
    logger.info("Merging revision '%s' in %s ..", revision, format_path(
        self.local))
    try:
        self.context.execute(*self.get_merge_command(revision))
    except ExternalCommandFailed as e:
        conflicts = self.merge_conflicts
        if conflicts:
            explanation = format('Merge failed due to conflicts in %s! (%s)',
                pluralize(len(conflicts), 'file'), concatenate(sorted(
                conflicts)))
            logger.warning('%s', explanation)
            if self.merge_conflict_handler(e):
                return
            else:
                raise MergeConflictError(explanation)
        else:
            raise