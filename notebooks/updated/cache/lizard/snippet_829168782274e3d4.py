def remove_child(self, child):
    try:
        self.children.remove(child)
    except ValueError as e:
        raise TreeError('child not found')
    else:
        child.up = None
        return child