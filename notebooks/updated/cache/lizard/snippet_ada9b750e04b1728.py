def handle_signal(self, signum, frame):
    if signum == signal.SIGINT:
        logging.info('shut down cleanly')
        asyncio.ensure_future(self.apply_command(globals.ExitCommand()))
    elif signum == signal.SIGUSR1:
        if isinstance(self.current_buffer, SearchBuffer):
            self.current_buffer.rebuild()
            self.update()