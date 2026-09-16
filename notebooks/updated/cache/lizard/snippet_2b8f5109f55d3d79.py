def __crawler_stop(self):
    if self.__stopping:
        return
    self.__stopping = True
    self.__wait_for_current_threads()
    self.queue.move_bulk([QueueItem.STATUS_QUEUED, QueueItem.
        STATUS_IN_PROGRESS], QueueItem.STATUS_CANCELLED)
    self.__crawler_finish()
    self.__stopped = True