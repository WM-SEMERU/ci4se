def get_ancestors(self):
    ancestors = []
    if self._meta.proxy_for_model:
        cls = self.__class__
        node = self
        while node.parent_id:
            node = cls.objects.get(pk=node.parent_id)
            ancestors.insert(0, node)
    else:
        node = self.parent
        while node:
            ancestors.insert(0, node)
            node = node.parent
    return ancestors