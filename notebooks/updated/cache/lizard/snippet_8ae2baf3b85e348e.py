def get_mesh_id(nlm_mesh):
    url_nlm2mesh = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    params = {'db': 'mesh', 'term': nlm_mesh, 'retmode': 'JSON'}
    r = requests.get(url_nlm2mesh, params=params)
    res = r.json()
    mesh_id = res['esearchresult']['idlist'][0]
    return mesh_id