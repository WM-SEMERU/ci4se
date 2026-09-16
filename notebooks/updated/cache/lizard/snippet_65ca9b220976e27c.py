def search(query, num_results=10):
    data = download(query, num_results)
    results = re.findall('\\<h3.*?\\>.*?\\<\\/h3\\>', data, re.IGNORECASE)
    if results is None or len(results) == 0:
        print('No results where found. Did the rate limit exceed?')
        return []
    links = []
    for r in results:
        mtch = re.match('.*?a\\s*?href=\\"(.*?)\\".*?\\>(.*?)\\<\\/a\\>.*$',
            r, flags=re.IGNORECASE)
        if mtch is None:
            continue
        url = mtch.group(1)
        url = re.sub('^.*?=', '', url, count=1)
        url = re.sub('\\&amp.*$', '', url, count=1)
        url = unquote(url)
        name = prune_html(mtch.group(2))
        name = convert_unicode(name)
        if is_url(url):
            links.append((name, url))
    return links