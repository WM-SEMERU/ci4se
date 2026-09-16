def fetch(self, force=False):
    tmpdir = tempfile.mkdtemp()
    fetch_results = {'core': os.path.join(tmpdir, 'insights-core.egg'),
        'gpg_sig': os.path.join(tmpdir, 'insights-core.egg.asc')}
    logger.debug('Beginning core fetch.')
    egg_url = self.config.egg_path
    egg_gpg_url = self.config.egg_gpg_path
    if egg_url is None:
        if self.config.legacy_upload:
            egg_url = '/v1/static/core/insights-core.egg'
        else:
            egg_url = '/static/insights-core.egg'
    if egg_gpg_url is None:
        if self.config.legacy_upload:
            egg_gpg_url = '/v1/static/core/insights-core.egg.asc'
        else:
            egg_gpg_url = '/static/insights-core.egg.asc'
    updated = self._fetch(egg_url, constants.core_etag_file, fetch_results[
        'core'], force)
    if updated:
        logger.debug('New core was fetched.')
        logger.debug('Beginning fetch for core gpg signature.')
        self._fetch(egg_gpg_url, constants.core_gpg_sig_etag_file,
            fetch_results['gpg_sig'], force)
        return fetch_results