def save(self, processes=1, manifests=False):
    if not self.path:
        raise BagError('Bag does not have a path.')
    old_dir = os.path.abspath(os.path.curdir)
    os.chdir(self.path)
    if manifests:
        unbaggable = _can_bag(self.path)
        if unbaggable:
            logger.error(
                'no write permissions for the following directories and files: \n%s'
                , unbaggable)
            raise BagError('Not all files/folders can be moved.')
        unreadable_dirs, unreadable_files = _can_read(self.path)
        if unreadable_dirs or unreadable_files:
            if unreadable_dirs:
                logger.error(
                    'The following directories do not have read permissions: \n%s'
                    , unreadable_dirs)
            if unreadable_files:
                logger.error(
                    'The following files do not have read permissions: \n%s',
                    unreadable_files)
            raise BagError(
                'Read permissions are required to calculate file fixities.')
        oxum = None
        self.algs = list(set(self.algs))
        for alg in self.algs:
            logger.info('updating manifest-%s.txt', alg)
            oxum = _make_manifest('manifest-%s.txt' % alg, 'data',
                processes, alg)
        logger.info('updating %s', self.tag_file_name)
        if oxum:
            self.info['Payload-Oxum'] = oxum
    _make_tag_file(self.tag_file_name, self.info)
    for alg in self.algs:
        _make_tagmanifest_file(alg, self.path)
    self._load_manifests()
    os.chdir(old_dir)