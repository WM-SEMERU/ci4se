def insert_after(self, target):
    if not target.parent:
        return
    target.parent.insert(target.parent.sprites.index(target) + 1, self)