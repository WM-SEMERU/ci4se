def chambers(self):
    return set(sorted([d.chamber for d in self.documents.all()]))