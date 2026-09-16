def get_pmid(doc_id):
    url_pmid = 'https://www.ebi.ac.uk/chembl/api/data/document.json'
    params = {'document_chembl_id': doc_id}
    res = requests.get(url_pmid, params=params)
    js = res.json()
    pmid = str(js['documents'][0]['pubmed_id'])
    return pmid