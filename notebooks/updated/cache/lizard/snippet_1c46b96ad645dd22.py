def parse(self, limit=None):
    if limit is not None:
        LOG.info('Only parsing first %s rows fo each file', str(limit))
    LOG.info('Parsing files...')
    self._process_straininfo(limit)
    self._process_ontology_mappings_file(limit)
    self._process_measurements_file(limit)
    self._process_strainmeans_file(limit)
    self._fill_provenance_graph(limit)
    LOG.info('Finished parsing.')
    return