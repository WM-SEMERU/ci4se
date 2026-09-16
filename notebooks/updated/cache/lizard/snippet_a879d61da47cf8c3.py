def get_child_pos(self, child):
    for c, pos in self.children:
        if child == c:
            return pos