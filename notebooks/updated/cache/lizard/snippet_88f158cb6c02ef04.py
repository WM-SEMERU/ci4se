def get_metadata_for_ids(pmid_list, get_issns_from_nlm=False, get_abstracts
    =False, prepend_title=False):
    if len(pmid_list) > 200:
        raise ValueError('Metadata query is limited to 200 PMIDs at a time.')
    params = {'db': 'pubmed', 'retmode': 'xml', 'id': pmid_list}
    tree = send_request(pubmed_fetch, params)
    if tree is None:
        return None
    return get_metadata_from_xml_tree(tree, get_issns_from_nlm,
        get_abstracts, prepend_title)