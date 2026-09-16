def from_url(url, timeout=None):
    articles = NewsPlease.from_urls([url], timeout=timeout)
    if url in articles.keys():
        return articles[url]
    else:
        return None