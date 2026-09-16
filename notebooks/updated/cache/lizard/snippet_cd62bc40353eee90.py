def get_issns_for_journal(nlm_id):
    params = {'db': 'nlmcatalog', 'retmode': 'xml', 'id': nlm_id}
    tree = send_request(pubmed_fetch, params)
    if tree is None:
        return None
    issn_list = tree.findall('.//ISSN')
    issn_linking = tree.findall('.//ISSNLinking')
    issns = issn_list + issn_linking
    if not issns:
        return None
    else:
        return [issn.text for issn in issns]