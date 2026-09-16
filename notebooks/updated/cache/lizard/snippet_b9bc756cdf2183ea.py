def begin_recording(self):
    logger.info('[RewardProxyServer] [%d] Starting recording', self.id)
    if self._closed:
        logger.error(
            '[RewardProxyServer] [%d] Attempted to start writing although client connection is already closed. Aborting'
            , self.id)
        self.close()
        return
    if self._n_open_files != 0:
        logger.error(
            '[RewardProxyServer] [%d] WARNING: n open rewards files = %s. This is unexpected. Dropping connection.'
            , self.id, self._n_open_files)
        self.close()
        return
    logfile_path = os.path.join(self.factory.logfile_dir, 'rewards.demo')
    logger.info('Recording to {}'.format(logfile_path))
    self.file = open(logfile_path, 'w')
    self._n_open_files += 1
    logger.info('[RewardProxyServer] [%d] n open rewards files incremented: %s'
        , self.id, self._n_open_files)
    self.file.write(json.dumps({'version': 1, '_debug_version': '0.0.1'}))
    self.file.write('\n')
    self.file.flush()
    logger.info('[RewardProxyServer] [%d] Wrote version number', self.id)