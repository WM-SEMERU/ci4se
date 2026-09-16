def descendants(self, node):
    self._ensure_parameters()
    return CTEQuerySet(self.model, using=self._db, offset=node).exclude(pk=
        node.pk)