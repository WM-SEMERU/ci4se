def _get_update_artifact_cache_work(self, vts_artifactfiles_pairs):
    cache = self._cache_factory.get_write_cache()
    if cache:
        if len(vts_artifactfiles_pairs) == 0:
            return None
        targets = set()
        for vts, _ in vts_artifactfiles_pairs:
            targets.update(vts.targets)
        self._report_targets('Caching artifacts for ', list(targets), '.',
            logger=self.context.log.debug)
        always_overwrite = self._cache_factory.overwrite()
        args_tuples = []
        for vts, artifactfiles in vts_artifactfiles_pairs:
            overwrite = (always_overwrite or vts.cache_key in self.
                _cache_key_errors)
            args_tuples.append((cache, vts.cache_key, artifactfiles, overwrite)
                )
        return Work(lambda x: self.context.subproc_map(call_insert, x), [(
            args_tuples,)], 'insert')
    else:
        return None