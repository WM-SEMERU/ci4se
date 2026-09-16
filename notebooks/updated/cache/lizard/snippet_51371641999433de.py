def get_or_create_element(self, ns, name):
    if len(self._node.xpath('%s:%s' % (ns, name), namespaces=SLDNode._nsmap)
        ) == 1:
        return getattr(self, name)
    return self.create_element(ns, name)