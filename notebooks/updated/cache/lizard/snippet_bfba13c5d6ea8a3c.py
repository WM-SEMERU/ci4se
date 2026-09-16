def empty_directory(self):
    for child in self.walkfiles():
        child.remove()
    for child in reversed([d for d in self.walkdirs()]):
        if child == self or not child.isdir():
            continue
        child.rmdir()