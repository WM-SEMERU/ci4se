def start(self):
    old_start_count = self.__start_count
    self.__start_count += 1
    if old_start_count == 0:
        self.data_channel_start_event.fire()