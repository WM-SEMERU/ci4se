def start(self):
    super().start()
    comments_thread = BotThread(name='{}-comments-stream-thread'.format(
        self._name), target=self._listen_comments)
    comments_thread.start()
    self._threads.append(comments_thread)
    self.log.info('Starting comments stream ...')