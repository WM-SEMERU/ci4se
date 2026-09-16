def execute(command, working_directory=config.BASE_DIR, stderr=sp.STDOUT):
    LOG.info('Executing in %s ...', working_directory)
    LOG.info(command)
    sp.check_call(command, cwd=working_directory, stderr=stderr, shell=True)