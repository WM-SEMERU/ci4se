def current_codes_from_pdb():
    url = 'http://www.rcsb.org/pdb/rest/getCurrent'
    r = requests.get(url)
    if r.status_code == 200:
        pdb_codes = [x.lower() for x in r.text.split('"') if len(x) == 4]
    else:
        print('Request for {0} failed with status code {1}'.format(url, r.
            status_code))
        return
    return pdb_codes