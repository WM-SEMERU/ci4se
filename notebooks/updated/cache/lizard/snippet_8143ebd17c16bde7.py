def increase_by_changes(self, changes_amount, ratio):
    increases = round(changes_amount * ratio)
    return self.increase(int(increases))