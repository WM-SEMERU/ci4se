def parse(path):
    doc = ET.parse(path).getroot()
    channel = doc.find('./channel')
    blog = _parse_blog(channel)
    authors = _parse_authors(channel)
    categories = _parse_categories(channel)
    tags = _parse_tags(channel)
    posts = _parse_posts(channel)
    return {'blog': blog, 'authors': authors, 'categories': categories,
        'tags': tags, 'posts': posts}