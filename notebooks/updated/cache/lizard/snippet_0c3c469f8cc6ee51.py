def time_in_range(self):
    curr = datetime.datetime.now().time()
    if self.start_time <= self.end_time:
        return self.start_time <= curr <= self.end_time
    else:
        return self.start_time <= curr or curr <= self.end_time