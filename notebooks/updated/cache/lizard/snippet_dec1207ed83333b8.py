def remove(self, child):
    try:
        if self.element == child.traversal_parent:
            self._remove_from_traversal_index(child)
        else:
            self._remove_from_index(child)
            self.list.remove(child)
    except:
        raise