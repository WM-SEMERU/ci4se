def _get_online_chapter(self, book_name, book_chapter, cache_chapter):
    url = self.build_recovery_online_url(book_name, book_chapter)
    logging.debug('Looking up chapter at URL: {}'.format(url))
    r = requests.get(url)
    if r.status_code != 200:
        logging.error('Could not look up {} {} at URL {}'.format(book_name,
            book_chapter, url))
        raise Exception('Could not look up {} {} at URL {}'.format(
            book_name, book_chapter, url))
    chapter_html = r.text
    soup = BeautifulSoup(chapter_html, 'html.parser')
    verses_list_soup = soup.get_text().split('\n')
    verses_list = []
    verse_num = 1
    for verse in verses_list_soup:
        verse = self._remove_non_ascii(verse)
        if re.search('[0-9]+:[0-9]+', verse):
            verses_list.append(re.sub('[0-9]+:[0-9]+', str(verse_num) + '.',
                verse))
            verse_num += 1
    logging.debug('Successfully built list for {} chapter {}'.format(
        book_name, book_chapter))
    if cache_chapter:
        base_dir = os.path.expanduser('~/.diyr')
        book_dir = '{}/{}'.format(base_dir, book_name)
        chapter_file = '{}/{}'.format(book_dir, book_chapter)
        if not os.path.isdir(base_dir):
            os.mkdir(base_dir)
        if not os.path.isdir(book_dir):
            os.mkdir(book_dir)
        if not os.path.isfile(chapter_file):
            f = open(chapter_file, 'w')
            f.write('\n'.join(verses_list))
            f.close()
    return verses_list