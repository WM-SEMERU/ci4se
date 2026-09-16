def at_depth(self, depth):
    for child in list(self.children):
        if depth == 0:
            yield child
        else:
            for grandchild in child.at_depth(depth - 1):
                yield grandchild