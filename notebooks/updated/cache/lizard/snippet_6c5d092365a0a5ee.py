def clone(self):
    logger.debug('')
    if not self.url:
        estr = 'Cannot install this repos without a URL. %s' % self.info()
        logger.warning(estr)
        raise ValueError(estr)
    url = urlparse(self.url)
    url_path = url[2]
    path_end = url_path.split('/')
    path_end = path_end[len(path_end) - 1]
    if url.scheme not in self.supported_schemes:
        raise ValueError("Unsupported scheme '{}' for {}".format(url.scheme,
            self.url))
    assert self.repo_dir, 'Invalid repo directory.'
    logger.debug('cloning %s into %s .', self.url, self.repo_dir)
    self.pr_pass('\nInstalling %s ... ' % self.url)
    p = git.clone('--progress', self.url, self.repo_dir, _out=self.
        _sh_stdout('blue'), _err=self._sh_stderr('blue'))
    p.wait()