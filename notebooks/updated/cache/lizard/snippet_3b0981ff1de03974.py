def create_request(query):
    yarr_url = app.config.get('YARR_URL', False)
    if not yarr_url:
        raise 'No URL to Yarr! server specified in config.'
    api_token = app.config.get('YARR_API_TOKEN', False)
    headers = {'X-API-KEY': api_token} if api_token else {}
    payload = {'q': query}
    url = '%s/search' % yarr_url
    return requests.get(url, params=payload, headers=headers)