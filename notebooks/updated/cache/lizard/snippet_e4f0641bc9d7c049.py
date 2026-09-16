def get_rating(self):
    if not (self.votes and self.score):
        return 0
    return float(self.score) / (self.votes + self.field.weight)