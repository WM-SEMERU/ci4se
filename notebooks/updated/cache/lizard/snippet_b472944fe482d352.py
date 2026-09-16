def _create_parser(self, html_parser, current_url):
    css_code = ''
    elements = html_parser.find('style,link[rel="stylesheet"]').list_results()
    for element in elements:
        if element.get_tag_name() == 'STYLE':
            css_code = css_code + element.get_text_content()
        else:
            css_code = css_code + requests.get(urljoin(current_url, element
                .get_attribute('href'))).text
    self.stylesheet = tinycss.make_parser().parse_stylesheet(css_code)