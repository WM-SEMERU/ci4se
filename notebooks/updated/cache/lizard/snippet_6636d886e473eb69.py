def str(self, local):
    s = self.start_time.str(local) + ' to ' + self.end_time.str(local)
    return s