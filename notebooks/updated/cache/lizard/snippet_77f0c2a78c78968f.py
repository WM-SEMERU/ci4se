def random_post(subreddit, apikey):
    subreddit = '/r/random' if subreddit is None else '/r/%s' % subreddit
    urlstr = 'http://reddit.com%s/random?%s' % (subreddit, time.time())
    url = get(urlstr, headers={'User-Agent': 'CslBot/1.0'}).url
    return '** %s - %s' % (get_title(url, apikey), get_short(url, apikey))