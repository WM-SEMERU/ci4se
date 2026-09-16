def browse_nodes(self):
    root = self._safe_get_element('BrowseNodes')
    if root is None:
        return []
    return [AmazonBrowseNode(child) for child in root.iterchildren()]