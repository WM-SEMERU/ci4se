def __event_exist(self, event_type):
    for i in range(self.len()):
        if self.events_list[i][1] < 0 and self.events_list[i][3] == event_type:
            return i
    return -1