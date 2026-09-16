def HasIndex(self, index):
    for i in self.Items:
        if i.index == index:
            return True
    return False