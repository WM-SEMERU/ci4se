def insert(self, index, child, by_name_index=-1):
    if self._can_add_child(child):
        try:
            if by_name_index == -1:
                self.indexes[child.name].append(child)
            else:
                self.indexes[child.name].insert(by_name_index, child)
        except KeyError:
            self.indexes[child.name] = [child]
        self.list.insert(index, child)