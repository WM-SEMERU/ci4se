def search_genotype_phenotype(self, phenotype_association_set_id=None,
    feature_ids=None, phenotype_ids=None, evidence=None):
    request = protocol.SearchGenotypePhenotypeRequest()
    request.phenotype_association_set_id = phenotype_association_set_id
    if feature_ids:
        request.feature_ids.extend(feature_ids)
    if phenotype_ids:
        request.phenotype_ids.extend(phenotype_ids)
    if evidence:
        request.evidence.extend(evidence)
    request.page_size = pb.int(self._page_size)
    self._logger.debug('search_genotype_phenotype {}'.format(request))
    return self._run_search_request(request, 'featurephenotypeassociations',
        protocol.SearchGenotypePhenotypeResponse)