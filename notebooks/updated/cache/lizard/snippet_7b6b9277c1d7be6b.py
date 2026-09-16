def _process_pubmed_ids(pubmed_ids):
    if pubmed_ids.strip() == '':
        id_list = []
    else:
        id_list = pubmed_ids.split('|')
    for i, val in enumerate(id_list):
        id_list[i] = 'PMID:' + val
    return id_list