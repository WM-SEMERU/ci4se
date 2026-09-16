def getAllowedReturnURLs(relying_party_url):
    rp_url_after_redirects, return_to_urls = services.getServiceEndpoints(
        relying_party_url, _extractReturnURL)
    if rp_url_after_redirects != relying_party_url:
        raise RealmVerificationRedirected(relying_party_url,
            rp_url_after_redirects)
    return return_to_urls