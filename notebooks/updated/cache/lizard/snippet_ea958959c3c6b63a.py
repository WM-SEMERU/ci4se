def count_publishingcountries(country, **kwargs):
    url = gbif_baseurl + 'occurrence/counts/publishingCountries'
    out = gbif_GET(url, {'country': country}, **kwargs)
    return out