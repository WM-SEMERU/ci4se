def _ExtractYahooSearchQuery(self, url):
    if 'p=' not in url:
        return None
    _, _, line = url.partition('p=')
    before_and, _, _ = line.partition('&')
    if not before_and:
        return None
    yahoo_search_url = before_and.split()[0]
    return yahoo_search_url.replace('+', ' ')