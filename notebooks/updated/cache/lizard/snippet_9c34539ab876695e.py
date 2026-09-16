def parse_feed(content):
    feed = feedparser.parse(content)
    articles = []
    for entry in feed['entries']:
        article = {'title': entry['title'], 'link': entry['link']}
        try:
            article['media'] = entry['media_content'][0]['url']
        except KeyError:
            article['media'] = None
        articles.append(article)
    return articles