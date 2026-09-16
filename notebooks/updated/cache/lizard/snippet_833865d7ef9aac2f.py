def get_percent(self):
    if not (self.votes and self.score):
        return 0
    return 100 * (self.get_rating() / self.field.range)