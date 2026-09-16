def _release(self):
    pypiconfig = pypi.PypiConfig()
    main_files = os.listdir(self.data['workingdir'])
    if 'setup.py' not in main_files and 'setup.cfg' not in main_files:
        default_answer = False
    else:
        default_answer = pypiconfig.want_release()
    if not utils.ask(
        'Check out the tag (for tweaks or pypi/distutils server upload)',
        default=default_answer):
        return
    package = self.vcs.name
    version = self.data['new_version']
    logger.info('Doing a checkout...')
    self.vcs.checkout_from_tag(version)
    self.data['tagdir'] = os.path.realpath(os.getcwd())
    logger.info('Tag checkout placed in %s', self.data['tagdir'])
    if self.setup_cfg.has_bad_commands():
        logger.info('This is not advisable for a release.')
        if utils.ask('Fix %s (and commit to tag if possible)' % self.
            setup_cfg.config_filename, default=True):
            self.setup_cfg.fix_config()
    sdist_options = self._sdist_options()
    if 'setup.py' in os.listdir(self.data['tagdir']):
        self._upload_distributions(package, sdist_options, pypiconfig)
    os.chdir(self.vcs.workingdir)