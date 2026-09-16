def join_cwd(self, path=None):
    if self.working_dir:
        logger.debug("'%s' instance 'working_dir' set to '%s' for join_cwd",
            type(self).__name__, self.working_dir)
        cwd = self.working_dir
    else:
        cwd = getcwd()
        logger.debug(
            "'%s' instance 'working_dir' unset; default to process '%s' for join_cwd"
            , type(self).__name__, cwd)
    if path:
        return join(cwd, path)
    return cwd