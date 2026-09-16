def add_link(self, rel, value, href=None):
    links_node = self.metadata.find('links')
    if links_node is None:
        links_node = ioc_et.make_links_node()
        self.metadata.append(links_node)
    link_node = ioc_et.make_link_node(rel, value, href)
    links_node.append(link_node)
    return True