def xml2object(self, content):
    r
    content = self.xml_filter(content)
    element = ET.fromstring(content)
    tree = self.parse(element) if self.__options['strip_attr'
        ] else self.parse_full(element)
    if not self.__options['strip_root']:
        node = self.get_node(element)
        if not self.__options['strip_attr']:
            tree['attrs'] = node['attr']
        return {node['tag']: tree}
    return tree