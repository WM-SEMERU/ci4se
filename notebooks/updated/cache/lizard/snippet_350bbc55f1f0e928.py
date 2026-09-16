def to_string(self):
    root = etree.Element('urlset', nsmap={None: SITEMAP_NS})
    for url in self.urls:
        url.generate(root)
    return etree.tostring(root, pretty_print=True, xml_declaration=True,
        encoding='utf-8')