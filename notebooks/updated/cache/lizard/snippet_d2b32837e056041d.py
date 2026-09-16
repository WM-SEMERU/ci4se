def insert_check(self, index, check_item):
    self.checks.insert(index, check_item)
    for other in self.others:
        other.insert_check(index, check_item)