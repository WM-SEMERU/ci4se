def get_service_url(region, endpoint_list, lookup):
    for endpoint in endpoint_list:
        region_get = endpoint.get('region', '')
        if region.lower() == region_get.lower():
            return http.parse_url(url=endpoint.get(lookup))
    else:
        raise exceptions.AuthenticationProblem(
            'Region "%s" was not found in your Service Catalog.', region)