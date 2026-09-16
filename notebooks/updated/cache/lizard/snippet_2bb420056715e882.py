def _ingest_sources(self, sources, stage, force=False):
    from concurrent import ingest_mp
    self.state = self.STATES.INGESTING
    downloadable_sources = [s for s in sources if force or s.is_processable and
        not s.is_ingested and not s.is_built]
    errors = 0
    with self.progress.start('ingest', stage, message='Ingesting ' + ('MP' if
        self.multi else 'SP'), item_total=len(sources), item_type='source',
        item_count=len(downloadable_sources)) as ps:
        for source in sources:
            _ = source.source_table
        if self.multi:
            args = [(self.identity.vid, stage, source.vid, force) for
                source in downloadable_sources]
            pool = self.library.process_pool(limited_run=self.limited_run)
            try:
                result = pool.map_async(ingest_mp, args, 1)
                pool.close()
                pool.join()
            except KeyboardInterrupt:
                self.log('Got keyboard interrrupt; terminating workers')
                pool.terminate()
                raise
        else:
            for i, source in enumerate(downloadable_sources, 1):
                ps.add(message='Ingesting source #{}, {}'.format(i, source.
                    name), source=source, state='running')
                r = self._ingest_source(source, ps, force)
                if not r:
                    errors += 1
        if errors > 0:
            from ambry.dbexceptions import IngestionError
            raise IngestionError('Failed to ingest {} sources'.format(errors))
    return errors