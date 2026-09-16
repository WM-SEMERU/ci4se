def getThread(self, name):
    if not name in self.thread_list:
        self.logger.error('Thread {0} is not registered!'.format(name))
        raise Exception('Thread {0} is not registered!'.format(name))
    return self.thread_list[name]