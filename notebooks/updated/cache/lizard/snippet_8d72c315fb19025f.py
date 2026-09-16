def AddRunsFromDirectory(self, path, name=None):
    logger.info('Starting AddRunsFromDirectory: %s (as %s)', path, name)
    for subdir in io_wrapper.GetLogdirSubdirectories(path):
        logger.info('Processing directory %s', subdir)
        if subdir not in self._run_loaders:
            logger.info('Creating DB loader for directory %s', subdir)
            names = self._get_exp_and_run_names(path, subdir, name)
            experiment_name, run_name = names
            self._run_loaders[subdir] = _RunLoader(subdir=subdir,
                experiment_name=experiment_name, run_name=run_name)
    logger.info('Done with AddRunsFromDirectory: %s', path)