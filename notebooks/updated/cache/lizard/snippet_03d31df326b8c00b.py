def find(self, name=None, ns_uri=None, first_only=False):
    if name is None:
        name = '*'
    if ns_uri is None:
        ns_uri = '*'
    impl_nodelist = self.adapter.find_node_elements(self.impl_node, name=
        name, ns_uri=ns_uri)
    if first_only:
        if impl_nodelist:
            return self.adapter.wrap_node(impl_nodelist[0], self.adapter.
                impl_document, self.adapter)
        else:
            return None
    return self._convert_nodelist(impl_nodelist)