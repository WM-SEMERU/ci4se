def get_take(self, max_take):
    if self.take == None:
        return max_take
    if self.take < 0:
        return 0
    if self.take > max_take:
        return max_take
    return self.take