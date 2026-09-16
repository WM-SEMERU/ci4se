def parse_code_ul(self, url, ul):
    li_list = ul.find_all('li', recursive=False)
    li = li_list[0]
    span_title = li.find('span', attrs={'class': re.compile('TM\\d+Code')},
        recursive=False)
    section = Section(span_title.attrs['id'], span_title.text.strip())
    div_italic = li.find('div', attrs={'class': 'italic'}, recursive=False)
    if div_italic:
        section.content = div_italic.text.strip()
    span_link = li.find('span', attrs={'class': 'codeLienArt'}, recursive=False
        )
    if span_link:
        a_link = span_link.find('a', recursive=False)
        if self.with_articles:
            service = self.section_service
            section.articles = service.articles(self.id_code, section.
                id_section, self.date_pub)
        else:
            section.articles = a_link.text.strip()
        section.url_section = cleanup_url(urljoin(url, a_link.attrs['href']))
    section.children = [self.parse_code_ul(url, child) for child in li.
        find_all('ul', recursive=False)]
    return section