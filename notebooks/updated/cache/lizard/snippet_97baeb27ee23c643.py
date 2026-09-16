def validate_urls(urls, allowed_response_codes=None):
    for url in urls:
        validate_url(url, allowed_response_codes=allowed_response_codes)
    return True