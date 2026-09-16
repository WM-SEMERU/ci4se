def tmdb_search_movies(api_key, title, year=None, adult=False, region=None,
    page=1, cache=True):
    url = 'https://api.themoviedb.org/3/search/movie'
    try:
        if year:
            year = int(year)
    except ValueError:
        raise MapiProviderException('year must be numeric')
    parameters = {'api_key': api_key, 'query': title, 'page': page,
        'include_adult': adult, 'region': region, 'year': year}
    status, content = _request_json(url, parameters, cache=cache)
    if status == 401:
        raise MapiProviderException('invalid API key')
    elif status != 200 or not any(content.keys()):
        raise MapiNetworkException('TMDb down or unavailable?')
    elif status == 404 or status == 422 or not content.get('total_results'):
        raise MapiNotFoundException
    return content