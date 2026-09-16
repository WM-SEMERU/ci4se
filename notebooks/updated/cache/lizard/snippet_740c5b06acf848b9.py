def run(self):
    while True:
        self.update_log_filenames()
        self.open_closed_files()
        anything_published = self.check_log_files_and_publish_updates()
        if not anything_published:
            time.sleep(0.05)