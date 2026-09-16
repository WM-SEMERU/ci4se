def execute(self):
    clean_cmd = ['git', 'clean', '-X', '-d']
    if 'CI' not in os.environ:
        LOGGER.info('The following files/directories will be deleted:')
        LOGGER.info('')
        LOGGER.info(check_output(clean_cmd + ['-n']).decode())
        if not strtobool(input('Proceed?: ')):
            return False
    check_call(clean_cmd + ['-f'])
    empty_dirs = self.get_empty_dirs(self.env_root)
    if empty_dirs != []:
        LOGGER.info('Now removing empty directories:')
    for directory in empty_dirs:
        LOGGER.info('Removing %s/', directory)
        shutil.rmtree(os.path.join(self.env_root, directory))
    return True