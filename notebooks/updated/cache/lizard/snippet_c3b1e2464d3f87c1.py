def insert(self, index, child):
    if child not in (None, self):
        if isinstance(child, String):
            child_parent = child._parent
            if self._parent is child:
                child.remove(self)
                if child_parent:
                    index = child_parent.children.index(child)
                    child_parent.remove(child)
                    child_parent.insert(index, self)
            elif child_parent:
                child_parent.remove(child)
            child._parent = self
        if index is None:
            self.children.append(child)
        else:
            self.children.insert(index, child)