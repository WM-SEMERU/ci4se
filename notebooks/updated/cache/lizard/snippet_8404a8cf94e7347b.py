def olderado_best_model(pdb_id):
    pdb_code = pdb_id[:4].lower()
    olderado_url = (
        'http://www.ebi.ac.uk/pdbe/nmr/olderado/searchEntry?pdbCode=' +
        pdb_code)
    olderado_page = download_decode(olderado_url, verbose=False)
    if olderado_page:
        parsed_page = BeautifulSoup(olderado_page, 'html.parser')
    else:
        return None
    try:
        best_model = parsed_page.find_all('td')[1]
    except IndexError:
        print(
            "No model info could be found for {0} - ensure that it's an NMR structure."
            .format(pdb_id))
        return None
    try:
        model_no = int(best_model.string)
    except ValueError as v:
        print('Did not find a number for best model.')
        raise v
    return model_no