def update(self, items):
    for parent, sub_item in _iterate_dependencies(items):
        dep = self._deps[sub_item]
        if parent not in dep.parent:
            dep.parent.append(parent)