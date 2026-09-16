def rollback(self):
    if not self._moved_paths.can_rollback:
        logger.error("Can't roll back %s; was not uninstalled", self.dist.
            project_name)
        return False
    logger.info('Rolling back uninstall of %s', self.dist.project_name)
    self._moved_paths.rollback()
    for pth in self.pth.values():
        pth.rollback()