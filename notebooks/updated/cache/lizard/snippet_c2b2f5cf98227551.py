def idle_task(self):
    if self.download_last_timestamp is not None and time.time(
        ) - self.download_last_timestamp > 0.7:
        self.download_last_timestamp = time.time()
        self.handle_log_data_missing()