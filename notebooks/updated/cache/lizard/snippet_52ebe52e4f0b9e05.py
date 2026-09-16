def wait_process(self):
    self.process.wait()
    if self.analyze_data:
        self.receiving_thread.join()