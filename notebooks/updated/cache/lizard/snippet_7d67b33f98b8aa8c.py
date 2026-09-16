def join(self, timeout=None):
    if self.__wait_for_finishing_thread:
        if not timeout:
            while True:
                self.__wait_for_finishing_thread.join(0.5)
                if not self.__wait_for_finishing_thread.isAlive():
                    break
        else:
            self.__wait_for_finishing_thread.join(timeout)
        return not self.__wait_for_finishing_thread.is_alive()
    else:
        logger.warning('Cannot join as state machine was not started yet.')
        return False