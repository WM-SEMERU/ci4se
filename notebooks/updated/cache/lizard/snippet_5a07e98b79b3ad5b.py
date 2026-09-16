def stop(self):
    thread = self.thread()
    if thread is not None:
        if self.stop_event() is not None:
            self.stop_event().set()
        self.thread_stopped()
        if self.stop_event() is not None:
            thread.join(self.join_timeout())
            self.close_thread()