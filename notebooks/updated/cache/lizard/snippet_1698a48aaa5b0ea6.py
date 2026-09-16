def release(self):
    self.__lock.release()
    with self.__condition:
        self.__condition.notify()