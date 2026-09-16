def search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=
    2.0, only_standard=False):
    global BeautifulSoup
    if BeautifulSoup is None:
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            from BeautifulSoup import BeautifulSoup
    hashes = set()
    query = quote_plus(query)
    get_page(url_home % vars())
    if start:
        if num == 10:
            url = url_next_page % vars()
        else:
            url = url_next_page_num % vars()
    elif num == 10:
        url = url_search % vars()
    else:
        url = url_search_num % vars()
    while not stop or start < stop:
        time.sleep(pause)
        html = get_page(url)
        soup = BeautifulSoup(html)
        anchors = soup.find(id='search').findAll('a')
        for a in anchors:
            if only_standard and (not a.parent or a.parent.name.lower() != 'h3'
                ):
                continue
            try:
                link = a['href']
            except KeyError:
                continue
            link = filter_result(link)
            if not link:
                continue
            h = hash(link)
            if h in hashes:
                continue
            hashes.add(h)
            yield link
        if not soup.find(id='nav'):
            break
        start += num
        if num == 10:
            url = url_next_page % vars()
        else:
            url = url_next_page_num % vars()