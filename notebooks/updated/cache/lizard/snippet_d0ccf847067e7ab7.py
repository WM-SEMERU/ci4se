def get_external_references(self):
    for ext_ref_node in self.node.findall('externalRef'):
        ext_refs_obj = CexternalReference(ext_ref_node)
        for ref in ext_refs_obj:
            yield ref