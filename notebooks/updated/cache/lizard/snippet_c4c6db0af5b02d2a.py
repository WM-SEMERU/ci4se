def start(self, aug='EventLoopThread'):
    if self.stopping:
        raise LoopStoppingError('Cannot perform action while loop is stopping.'
            )
    if not self.loop:
        self._logger.debug('Starting event loop')
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self._loop_thread_main, name=
            aug, daemon=True)
        self.thread.start()