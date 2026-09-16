def _raise_redirect_exceptions(response):
    if response.status_code not in [301, 302, 307]:
        return None
    new_url = urljoin(response.url, response.headers['location'])
    if 'reddits/search' in new_url:
        subreddit = new_url.rsplit('=', 1)[1]
        raise InvalidSubreddit('`{0}` is not a valid subreddit'.format(
            subreddit))
    elif not RE_REDIRECT.search(response.url):
        raise RedirectException(response.url, new_url)
    return new_url