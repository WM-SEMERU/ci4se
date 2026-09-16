def get_text_content_for_pmids(pmids):
    pmc_pmids = set(pmc_client.filter_pmids(pmids, source_type='fulltext'))
    pmc_ids = []
    for pmid in pmc_pmids:
        pmc_id = pmc_client.id_lookup(pmid, idtype='pmid')['pmcid']
        if pmc_id:
            pmc_ids.append(pmc_id)
        else:
            pmc_pmids.discard(pmid)
    pmc_xmls = []
    failed = set()
    for pmc_id in pmc_ids:
        if pmc_id is not None:
            pmc_xmls.append(pmc_client.get_xml(pmc_id))
        else:
            failed.append(pmid)
        time.sleep(0.5)
    remaining_pmids = set(pmids) - pmc_pmids | failed
    abstracts = []
    for pmid in remaining_pmids:
        abstract = pubmed_client.get_abstract(pmid)
        abstracts.append(abstract)
        time.sleep(0.5)
    return [text_content for source in (pmc_xmls, abstracts) for
        text_content in source if text_content is not None]