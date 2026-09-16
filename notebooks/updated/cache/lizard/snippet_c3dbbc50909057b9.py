def walk_tree(self, top=None):
    if top is None:
        top = self.rootgrp
    values = top.groups.values()
    yield values
    for value in top.groups.values():
        for children in self.walk_tree(value):
            yield children