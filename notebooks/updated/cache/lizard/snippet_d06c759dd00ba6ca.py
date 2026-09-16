def parse_html(infile, xpath):
    if not isinstance(infile, lh.HtmlElement):
        infile = lh.fromstring(infile)
    infile = infile.xpath(xpath)
    if not infile:
        raise ValueError('XPath {0} returned no results.'.format(xpath))
    return infile