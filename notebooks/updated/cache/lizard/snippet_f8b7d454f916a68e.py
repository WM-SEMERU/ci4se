def retrieve_all_pages(api_endpoint, **kwargs):
    page_size = getattr(settings, 'REQUEST_PAGE_SIZE', 20)
    loaded_results = []
    offset = 0
    while True:
        response = api_endpoint(limit=page_size, offset=offset, **kwargs)
        count = response.get('count', 0)
        loaded_results += response.get('results', [])
        if len(loaded_results) >= count:
            break
        offset += page_size
    return loaded_results