def google_average(search_term, num_results, api_key, cse_id, **kwargs):
    url_list = []
    result = {'name': search_term}
    GIS = GoogleImageSearch(api_key, cse_id)
    url_list = GIS.search(search_term, num_results)
    result.update(_image_search_average(url_list, **kwargs))
    return result