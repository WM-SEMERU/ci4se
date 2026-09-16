def update_with_increment_value(self, increment_value, mesg=None):
    self.cur_value += increment_value
    self.update(self.cur_value, mesg)