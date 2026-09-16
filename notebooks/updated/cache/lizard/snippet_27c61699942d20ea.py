def _get_unique_links(page_url, soup):
    if 'http://' not in page_url and 'https://' not in page_url:
        return []
    prefix = 'http:'
    if page_url.startswith('https:'):
        prefix = 'https:'
    simple_url = page_url.split('://')[1]
    base_url = simple_url.split('/')[0]
    full_base_url = prefix + '//' + base_url
    raw_links = []
    raw_unique_links = []
    links = soup.find_all('a')
    for link in links:
        raw_links.append(link.get('href'))
    img_links = soup.find_all('img')
    for img_link in img_links:
        raw_links.append(img_link.get('src'))
    links = soup.find_all('link')
    for link in links:
        raw_links.append(link.get('href'))
    img_links = soup.find_all('script')
    for img_link in img_links:
        raw_links.append(img_link.get('src'))
    for link in raw_links:
        if link not in raw_unique_links:
            raw_unique_links.append(link)
    unique_links = []
    for link in raw_unique_links:
        if link and len(link) > 1:
            if link.startswith('//'):
                link = prefix + link
            elif link.startswith('/'):
                link = full_base_url + link
            elif link.startswith('./'):
                link = full_base_url + link[1:]
            elif link.startswith('#'):
                link = full_base_url + link
            elif '//' not in link:
                link = full_base_url + '/' + link
            else:
                pass
            unique_links.append(link)
    return unique_links