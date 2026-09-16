def is_within(self, query, subject):
    if self.pt_within(query[0], subject) and self.pt_within(query[1], subject):
        return True
    return False