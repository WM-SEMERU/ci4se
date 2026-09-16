def __get_timemachine(self):
    if not self.__timemachine:
        self.__timemachine = TimeMachine(self.object_uid, step=self.id)
    return self.__timemachine.at(self.id)