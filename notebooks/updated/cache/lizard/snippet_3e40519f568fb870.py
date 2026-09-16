def parse_navigation_html_to_tree(html, id):

    def xpath(x):
        return html.xpath(x, namespaces=HTML_DOCUMENT_NAMESPACES)
    try:
        value = xpath('//*[@data-type="binding"]/@data-value')[0]
        is_translucent = value == 'translucent'
    except IndexError:
        is_translucent = False
    if is_translucent:
        id = TRANSLUCENT_BINDER_ID
    tree = {'id': id, 'title': xpath(
        '//*[@data-type="document-title"]/text()')[0], 'contents': [x for x in
        _nav_to_tree(xpath('//xhtml:nav')[0])]}
    return tree