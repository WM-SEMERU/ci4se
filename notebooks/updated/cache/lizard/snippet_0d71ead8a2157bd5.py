def get_sentence_xpath_tuples(filename_url_or_filelike, xpath_to_text=
    TEXT_FINDER_XPATH):
    parsed_html = get_html_tree(filename_url_or_filelike)
    try:
        xpath_finder = parsed_html.getroot().getroottree().getpath
    except AttributeError:
        xpath_finder = parsed_html.getroottree().getpath
    nodes_with_text = parsed_html.xpath(xpath_to_text)
    sent_xpath_pairs = [(('\n\n' + s, xpath_finder(n)) if e == 0 else (s,
        xpath_finder(n))) for n in nodes_with_text for e, s in enumerate(
        SENTENCE_TOKEN_PATTERN.split(BRACKET_PATTERN.sub('', ''.join(n.
        xpath('.//text()'))))) if s.endswith(tuple(SENTENCE_ENDING))]
    return sent_xpath_pairs