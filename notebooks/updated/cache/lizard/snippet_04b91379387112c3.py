def is_sorted(self, ranks=None):
    ranks = ranks or self.ranks
    return check_sorted(self, ranks)